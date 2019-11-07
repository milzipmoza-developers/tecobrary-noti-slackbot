# coding=utf-8
def parseNotify(wish_book_data):
    message = '주인님:face_with_cowboy_hat:, 새로운 희망 도서:book: 입니다.\n' \
              '\n' \
              ':one:제목 - {title}\n' \
              ':two:저자 - {author}\n' \
              ':three:출판사 - {publisher}\n' \
              ':four:ISBN - {isbn}\n' \
              '\n' \
              '빠르게 처리해주실꺼죠?:rocket:'
    formatted_message = message.format(title=wish_book_data['title'],
                                       author=wish_book_data['author'],
                                       publisher=wish_book_data['publisher'],
                                       isbn=wish_book_data['isbn'],
                                       createdAt=wish_book_data['createdAt'])
    return formatted_message


def parseEnrolled(enrolled_book_data):
    message = '여러분:face_with_cowboy_hat:, 테코브러리 신착 도서 알림 입니다!\n' \
              '\n' \
              ':one:제목 - {title}\n' \
              ':two:저자 - {author}\n' \
              ':three:출판사 - {publisher}\n'
    formatted_message = message.format(title=enrolled_book_data['title'],
                                       author=enrolled_book_data['author'],
                                       publisher=enrolled_book_data['publisher'])
    return formatted_message


def tecobraryInformation():
    return '주인님, 안녕하세요.\n' \
           '이용은 https://dgh7qtsxun9z8.cloudfront.net/\n' \
           '에서 가능합니다. 좋은 하루 보내세요~ :heart_eyes:\n'
