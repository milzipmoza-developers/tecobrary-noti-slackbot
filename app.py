# coding=utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route('/registered', methods=['post'])
def notification():
    wish_book_data = request.get_json()
    print(wish_book_data)
    print(wish_book_data['title'])
    print(wish_book_data['author'])
    print(wish_book_data['publisher'])
    print(wish_book_data['isbn'])
    return 'registered'


@app.route('/enrolled', methods=['post'])
def enrolled():
    enrolled_book_data = request.get_json()
    print(enrolled_book_data)
    print(enrolled_book_data['title'])
    print(enrolled_book_data['author'])
    print(enrolled_book_data['publisher'])
    print(enrolled_book_data['isbn'])
    return 'enrolled'
