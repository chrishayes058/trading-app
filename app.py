import config
import json
import requests
from chalice import Chalice

# Globals #
app = Chalice(app_name='trading')

# Functions #
@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    request = app.current_request
    webhook_message = request.json_body

    data = {
        "symbol": webhook_message['ticker'],
        "qty": 1,
        "side": "buy",
        "type": "limit",
        "limit_price": webhook_message['close'],
        "time_in_force": "gtc",
        "order_class": "bracket",
        "take_profit": {
            "limit_price": webhook_message['close'] * 1.05
        },
        "stop_loss": {
            "stop_price": webhook_message['close'] * 0.98
        }
    }

    r = requests.post(config.ORDERS_URL, json=data, headers=config.HEADERS)

    response = json.loads(r.content)

    return {
        'message': response,
        'webhook_message': webhook_message
    }


@app.route('/get_account_data')
def get_acccount_data():
    r = requests.get(config.ACCOUNT_URL, headers=config.HEADERS)
    response = json.loads(r.content)

    return response


@app.route('/get_orders')
def get_orders():
    r = requests.get(config.ORDERS_URL, headers=config.HEADERS)
    response = json.loads(r.content)

    return response

