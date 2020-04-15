import json
import os
import logging
from concurrent.futures import ThreadPoolExecutor
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import pprint
import websocket
from click.testing import CliRunner
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.exceptions import ApiError
from webexteamssdk.models.immutable import Message
from wibot.rbac import get_role
from wibot.cli.cli import firewall
from wibot.utils import get_config
from wibot import BOT_AUTH_HEADER

configs = get_config()

BOT_NAME = configs['BOT_NAME']
BOT_TOKEN = configs['BOT_TOKEN']

LOGGER = logging.getLogger(__name__)
API_URL = "https://api.ciscospark.com/v1/messages"
MAX_MSG_SIZE = 4096

api: WebexTeamsAPI = None
#changed max#workers to 1 to avoid message swap between concurrent calls
message_processor = ThreadPoolExecutor(max_workers=1)


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

def attachment_post(roomId : str, logtype: str):
    log_file_dir = '/logs/'
    print(log_file_dir)
    if logtype == 'embaudit':
        log_file_name = 'EmbConScan_log.txt'
    log_filepath = os.path.join(log_file_dir,log_file_name)
    print(log_filepath)
    m = MultipartEncoder({'roomId': roomId,
                          'text': 'Scan Results Attached',
                          'files': (log_filepath, open(log_filepath,'rb'),
                          'image/png')})

    headers={'Authorization': 'Bearer {}'.format(BOT_TOKEN),
    'Content-Type': m.content_type}

    response = requests.request('POST', API_URL, data=m, headers=headers)
    print(response)

    LOGGER.debug(pprint.pprint(response.json()))


def html_message_post(roomid: str, html: str):
    """Post a message to a spark room"""
    try:
        json_data = {"roomId": roomid,
                     "html": html}
        response = requests.request("POST", API_URL, json=json_data, headers=BOT_AUTH_HEADER).json()
        return response
    except Exception as e:
        LOGGER.error(str({'title': 'spark_message_post', 'exception': str(e)}))


def process_message(message):
    json_data = json.loads(message)
    if 'data' in json_data and \
        'activity' in json_data['data'] and \
        'id' in json_data['data']['activity']:
        message_id = json_data['data']['activity']['id']
        try:
            message: Message = api.messages.get(message_id)
            LOGGER.debug(message)
            if message.personId == api.people.me().id:
                return

            email = message.personEmail
            roles = get_role(email)
            if not roles:
                send_response(message.roomId, "Unauthorized user {}".format(email))
                return
            for role in roles:
                LOGGER.debug("Using role: {}".format(role))
                LOGGER.debug(message.text)
                runner = CliRunner()
                args = message.text.split()
                result = "Unauthorized user {}".format(email)
                if role == "storage":
                    result = runner.invoke(admin, args[1:] if not args[0] == BOT_NAME else args[2:])

                if role == "compute":
                    result = runner.invoke(compute, args[1:] if not args[0] == BOT_NAME else args[2:])

                if role == "customer":
                    result = runner.invoke(customer, args[1:] if not args[0] == BOT_NAME else args[2:])

                if role == "firewall":
                    if args[0] == BOT_NAME and args[1] == 'firewall' and args[2] == 'captures' and args[3] == 'asa':
                        greeting = "Please wait for ~30min-40min, scanning all FWs and contexts..."
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))                        
                        # Webex Teams has a limit on message size, so we need to chunk the output
                        #
                        split_output = result.output.split('\n')
                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''
                        if buf.strip():
                            send_response(message.roomId, buf)

                    elif args[0] == 'firewall' and args[1] == 'captures' and args [2] == 'asa':
                        greeting = "Please wait for ~30min-40min, scanning all FWs and contexts..."
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))                        
                        # Webex Teams has a limit on message size, so we need to chunk the output
                        #
                        split_output = result.output.split('\n')
                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''
                        if buf.strip():
                            send_response(message.roomId, buf)

                    elif args[0] == BOT_NAME and args[1] == 'firewall' and args[2] == 'captures' and args[3] == 'ftd':
                        greeting = "Please wait for a couple of minutes, scanning all FTDs ..."
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))                        
                        # Webex Teams has a limit on message size, so we need to chunk the output
                        # 
                        split_output = result.output.split('\n')
                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''
                        if buf.strip():
                            send_response(message.roomId, buf)
                    elif args[0] == 'firewall' and args[1] == 'captures' and args [2] == 'ftd':
                        greeting = "Please wait for a couple of minutes, scanning all FTDs ..."
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))                        
                        # Webex Teams has a limit on message size, so we need to chunk the output
                        # 
                        split_output = result.output.split('\n')
                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''
                        if buf.strip():
                            send_response(message.roomId, buf)
 
                    elif args[0] == BOT_NAME and args[1] == 'firewall' and args[2] == 'embaudit':
                        logtype=args[2]
                        greeting = "Please wait for ~1 hr, scanning EMBRYONIC Connection Settings on all ASAs"
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))                        
                        # Webex Teams has a limit on message size, so we need to chunk the output
                        #
                        split_output = result.output.split('\n')

                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''

                        if buf.strip():
                            send_response(message.roomId, buf)
                        attachment_post(message.roomId,logtype)

                    elif args[0] == 'firewall' and args[1] == 'embaudit':
                        logtype=args[1]
                        greeting = "Please wait for ~1 hr, scanning EMBRYONIC Connection Settings on all ASAs"
                        send_response(message.roomId, greeting)
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("Result Output {} Result ExitCode {}".format(result.output, result.exit_code))

                        # Webex Teams has a limit on message size, so we need to chunk the output
                        #
                        split_output = result.output.split('\n')
                        buf = ''
                        for line in split_output:
                            buf = buf + '\n' + line
                            if len(buf) > MAX_MSG_SIZE:
                                send_response(message.roomId, buf)
                                buf = ''

                        if buf.strip():
                            send_response(message.roomId, buf)   
                        attachment_post(message.roomId,logtype)

                    else:
                        result = runner.invoke(firewall, args[1:] if not args[0] == BOT_NAME else args[2:])
                        LOGGER.debug("{} {}".format(result.output, result.exit_code))
                         #
                         # Webex Teams has a limit on message size, so we need to chunk the output
                         #                 
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
