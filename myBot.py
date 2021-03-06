import requests
from time import sleep

import json
from flask import Flask
from flask import request
from flask import Response


url = "https://api.telegram.org/bot1477305025:AAHg-O4JTHEeFiNyRDGkbee_77SUuisQ3H0/"

app = Flask(__name__)


def get_updates_json(request, offset=None):

    response = requests.get(request + 'getUpdates',
                            data={'timeout': 100, 'offset': offset})

    return response.json()


def last_update(data):

    results = data['result']

    total_updates = len(results) - 1

    return results[total_updates]


def get_chat_id(update):

    chat_id = update['message']['chat']['id']

    return chat_id


def send_mess(chat, text):

    params = {'chat_id': chat, 'text': text}

    response = requests.post(url + 'sendMessage', data=params)

    return response


def sendKirIfKoon(r):
    msg = r['message']['text']
    chat_id = r['message']['chat']['id']
    if msg == 'koon':
        send_mess(chat_id, 'kir')


def write_json(data, fileName='response.json'):
    with open(fileName, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        write_json(msg, '11telegram_request.json')
        sendKirIfKoon(msg)
        return Response('ok', status=200)
    else:
        return "<h1>salam karbar</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
