import app
import config
import json
import requests
import websocket
import time
import _thread as thread
import threading

SOCKET = "wss://data.alpaca.markets/stream"
# websocket.enableTrace(True)  # More logging


class Stream:

    def __init__(self):
        self.mydata = threading.local()
        self.mydata.count = 0
        self.mydata.data = None
        self.mydata.ws = websocket.WebSocketApp(
            SOCKET,
            on_open=self.on_open,
            on_message=self.on_message,
            on_close=self.on_close
        )

    def on_open(self):
        # def run():
        print("Thread Opening")
        auth_data = {
            "action": "authenticate",
            "data": {
                "key_id": config.API_KEY,
                "secret_key": config.SECRET_KEY
            }
        }

        self.mydata.ws.send(json.dumps(auth_data))

        listen_message = {"action": "listen", "data": {"streams": ["T.TSLA"]}}
        self.mydata.ws.send(json.dumps(listen_message))
        listen_message = {"action": "listen", "data": {"streams": ["T.AAPL"]}}
        self.mydata.ws.send(json.dumps(listen_message))

    def on_message(self, json_message):
        self.mydata.count += 1
        print("received a message")
        message = json.loads(json_message)
        print(message.get("data"))

    def on_close(self):
        self.mydata.ws.close()
        print("closed connection")

    def start(self):
        self.mydata.ws.run_forever()


stream = Stream()
stream.start()
