# coding=utf-8
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request

import slack_api
from message_parser import parseNotify, parseEnrolled
from settings import REQUESTED_CHANNEL, ENROLLED_CHANNEL

app = Flask(__name__)


@app.route('/registered', methods=['post'])
def notification():
    wish_book_data = request.get_json()
    message = parseNotify(wish_book_data)
    app.logger.info(wish_book_data)
    response = slack_api.sendMessage(message, REQUESTED_CHANNEL)
    app.logger.info(response)
    return 'registered'


@app.route('/enrolled', methods=['post'])
def enrolled():
    enrolled_book_data = request.get_json()
    message = parseEnrolled(enrolled_book_data)
    app.logger.info(enrolled_book_data)
    response = slack_api.sendMessage(message, ENROLLED_CHANNEL)
    app.logger.info(response.json())
    return 'enrolled'


if __name__ == '__main__':
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1, mode='a')
    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
