import json
import logging
import pprint
from concurrent.futures import ThreadPoolExecutor
import requests
import websocket
from click.testing import CliRunner
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.exceptions import ApiError
from webexteamssdk.models.immutable import Message

from wibot import BOT_TOKEN, BOT_AUTH_HEADER, BOT_NAME
from wibot.cards import handle_doc
from wibot.cli import get_cli, HELP_TEXT
from wibot.rbac import get_role
from wibot.users import is_valid_webex_member

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.ERROR)
API_URL = "https://api.ciscospark.com/v1/messages"
MAX_MSG_SIZE = 4096

api: WebexTeamsAPI = None
message_processor = ThreadPoolExecutor(max_workers=1)


def send_raw_response(roomId: str, response_text: str):
    LOGGER.debug(f"Debug - Response Text: {response_text}")
    markdown = """
    \n{response}
    """.format(response=response_text)

    json_data = {
        'roomId': roomId,
        'markdown': markdown,
    }
    response = requests.request('POST', API_URL, json=json_data, headers=BOT_AUTH_HEADER)
    LOGGER.debug(f"Debug - Response: {pprint.pprint(response.json())}")


def send_response(roomId: str, response_text: str):
    markdown = """
    ```\n{response}
    """.format(response=response_text)

    json_data = {
        'roomId': roomId,
        'markdown': markdown,
    }
    response = requests.request('POST', API_URL, json=json_data, headers=BOT_AUTH_HEADER)
    LOGGER.debug(pprint.pprint(response.json()))


def send_card_response(roomId: str, card_response: str):
    json_data = {
        'roomId': roomId,
        'markdown': 'x',
        'attachments': [card_response],
    }
    pprint.pprint(json.dumps(json_data))
    response = requests.request('POST', API_URL, json=json_data, headers=BOT_AUTH_HEADER)
    LOGGER.debug(pprint.pprint(response.json()))


def invoke_command(args):
    runner = CliRunner()
    result = None
    cmd_args = args[1:] if not args[0] == BOT_NAME else args[2:]
    LOGGER.debug(f"Debug - CLI Arguments: {cmd_args}")

    cli = get_cli(args)
    LOGGER.debug(f"Debug - CLI Role: {cli}")

    if cli:
        LOGGER.debug(f"Debug - Executing CLI command...")
        result = runner.invoke(cli, cmd_args)

    LOGGER.debug(f"Debug - Command Result: {result}")
    return result


def handled_using_card(message, args) -> bool:
    if args and args[0] == BOT_NAME:
        args = args[1:]

    if args[0] != 'docs' or args[1:] is None:
        return False

    card_response = handle_doc(args[1])

    if not card_response:
        return False

    send_card_response(message.roomId, card_response)
    return True


def parse_args(message, admin_flag):
    args = message.text.split()
    if "membership" in args and ("add" in args or "pingteam" in args) and len(args) >= 3 and "-h" not in args:
        args.append(message.roomId)

        if "poke" in args and len(args) > 3:
            message = ' '.join(args[3:-1])
            del args[3:-1]
            args.append(message)

    args.append(admin_flag)

    return args


def process_message(message):
    json_data = json.loads(message)
    if 'data' in json_data and 'activity' in json_data['data'] and 'id' in json_data['data']['activity']:
        message_id = json_data['data']['activity']['id']
        LOGGER.debug(f"Debug - Message ID: {message_id}")
        try:
            message: Message = api.messages.get(message_id)
            LOGGER.debug(f"Debug - Message: {message}")
            if message.personId == api.people.me().id:
                return

            ''' Check if the invoker belongs to IaaS '''
            email = message.personEmail
            if not is_valid_webex_member(email):
                send_raw_response(message.roomId, f"*Unauthorized user: {email}*")
                return

            ''' Check if the invoker is firewall admin '''
            roles = get_role(email)
            admin_flag = 'False'
            if roles and roles[0] == 'admin':
                LOGGER.debug("Debug - Admin user {}... continuing".format(email))
                admin_flag = 'True'

            args = parse_args(message, admin_flag)
            if handled_using_card(message, args):
                return

            send_raw_response(message.roomId, "*processing...please wait*")
            LOGGER.debug(f"Debug - Input arguments: {args}")
            result = invoke_command(args)

            if result is None and "help" in args:
                split_output = HELP_TEXT.split('\n')
            elif result is None or result.exit_code != 0:
                LOGGER.error(f"Command failed with error: \n{result.output}")
                send_raw_response(message.roomId, f"Problem executing the command")
                split_output = HELP_TEXT.split('\n')
            else:
                # Webex Teams has a limit on message size, so we need to chunk the output
                split_output = result.output.split('\n')

            buf = ''
            for line in split_output:
                buf = buf + '\n' + line
                if len(buf) > MAX_MSG_SIZE:
                    send_response(message.roomId, buf)
                    buf = ''

            if buf.strip():
                send_response(message.roomId, buf)

        except ApiError:
            LOGGER.error("Unable to fetch message {}".format(message_id, json_data))


def on_message(ws, message):
    message_processor.submit(process_message, message)


def on_open(ws):
    LOGGER.debug('Opened received on ws')


def on_error(ws, err):
    LOGGER.error('Got a websocket error {}'.format(err))


def on_close(ws):
    LOGGER.info('Websocket closed')


class MessageHandler:

    def __init__(self, wss_url):
        websocket.enableTrace(True)
        header = {'Authorization:Bearer {}'.format(BOT_TOKEN)}
        self.ws = websocket.WebSocketApp(wss_url, on_open=on_open, on_message=on_message,
                                         on_close=on_close, on_error=on_error, header=header)

    def run_forever(self):
        LOGGER.info("Running websocket listener forever")
        global api
        api = WebexTeamsAPI(access_token=BOT_TOKEN)

        self.ws.run_forever()