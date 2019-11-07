# coding=utf-8
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request, make_response

import slack_api
from message_template import parseNotify, parseEnrolled, tecobraryInformation
from settings import REQUESTED_CHANNEL, ENROLLED_CHANNEL

app = Flask(__name__)


@app.route('/registered', methods=['post'])
def notification():
    wish_book_data = request.get_json()
    message = parseNotify(wish_book_data)
    app.logger.info(wish_book_data)
    response = slack_api.sendMessage(message, REQUESTED_CHANNEL)
    app.logger.info(response.json())
    return 'registered'


@app.route('/enrolled', methods=['post'])
def enrolled():
    enrolled_book_data = request.get_json()
    message = parseEnrolled(enrolled_book_data)
    app.logger.info(enrolled_book_data)
    response = slack_api.sendMessage(message, ENROLLED_CHANNEL)
    app.logger.info(response.json())
    return 'enrolled'


@app.route('/infos', methods=['GET', 'POST'])
def urls():
    # 메시지를 보낸다.
    slack_event = request.get_json()
    app.logger.info('slack_event', slack_event)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("event not found", 404, {"X-Slack-No-Retry": 1})


def event_handler(event_type, slack_event):
    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        message = tecobraryInformation()
        response = slack_api.sendMessage(message, channel)
        app.logger.info(response.json())
        return make_response("send mention message successfully", 200, {"content_type": "application/json"})
    message = "cannot handle this event [%s]" % event_type
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


if __name__ == '__main__':
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1, mode='a')
    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(debug=True, host='0.0.0.0')
