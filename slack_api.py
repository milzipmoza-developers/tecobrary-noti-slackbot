import requests

from settings import AUTH_TOKEN


def sendMessage(message, channel):
    headers = {
        'Content-Type': 'application/json;utf-8',
        'Authorization': 'Bearer ' + AUTH_TOKEN
    }
    body = {
        'channel': channel,
        'text': message
    }
    response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=body)
    return response
