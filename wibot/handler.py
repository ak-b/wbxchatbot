import json
import logging
from concurrent.futures import ThreadPoolExecutor
import requests
import pprint
import websocket
from click.testing import CliRunner
from webexteamssdk import WebexTeamsAPI
from webexteamssdk.exceptions import ApiError
from webexteamssdk.models.immutable import Message
from wistorage.cli.cli import main

from wibot import BOT_TOKEN, BOT_AUTH_HEADER, BOT_NAME

LOGGER = logging.getLogger(__name__)
API_URL = "https://api.ciscospark.com/v1/messages"

api: WebexTeamsAPI = None
message_processor = ThreadPoolExecutor(max_workers=4)


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


def process_message(message):
    json_data = json.loads(message)
    LOGGER.debug(pprint.pprint(json_data))
    if 'data' in json_data and \
        'activity' in json_data['data'] and \
        'id' in json_data['data']['activity']:
        message_id = json_data['data']['activity']['id']
        try:
            message: Message = api.messages.get(message_id)
            if message.personId == api.people.me().id:
                return
            LOGGER.debug(message.text)
            runner = CliRunner()
            args = message.text.split()
            result = runner.invoke(main, args if not args[0] == BOT_NAME else args[1:])
            LOGGER.debug("{} {}".format(result.output, result.exit_code))
            send_response(message.roomId, result.output)
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
