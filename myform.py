from os.path import exists

from bottle import post, request, route, view
from re import compile as regex_compile
from routes import base_page, menu
import json


# функция для проверки почты
def is_valid_email(email: str) -> bool:
    email_pattern = regex_compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    arr = email.split('@')
    return bool(email_pattern.match(email)) and len(arr[0]) <= 64 and len(arr[1]) <= 255


# функция для проверки заголовка
def is_valid_title(title: str) -> bool:
    return title != "" and 20 <= len(title) <= 100


# функция для проверки описания
def is_valid_description(description: str) -> bool:
    return description != "" and 60 <= len(description) <= 1000


# функция для проверки никнейма
def is_valid_nickname(nickname: str) -> bool:
    nickname_pattern = regex_compile(r"^\w{3,16}$")
    return bool(nickname_pattern.match(nickname))

def isCorrectMail(email: str):
    pattern = regex_compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if pattern.match(email):
        return True
    else:
        return False


@route('/form')
@view('form')
def form():
    return base_page(dict(title='Форма',
                          menu=menu(4)))


@post('/form', method='post')
def my_form():
    email = request.forms.get('email')
    question = request.forms.get('question')

    if not isCorrectMail(email):
        return f"Ошибка: email не соответствует шаблону"
    elif question == "":
        return f"Ошибка: введите ваш вопрос"

    # pdb.set_trace()
    questions = {}
    if exists('question.json'):
        with open('question.json', 'r', encoding='utf-8') as read_json:
            questions = json.load(read_json)

    with open('question.json', 'w', encoding='utf-8') as write_json:
        if email in questions:
            questions.get(email).append(question)
        else:
            questions[email] = [question]
        json.dump(questions, write_json)

    return f"Спасибо! Ответ будет отправлен на почту: {email}!"
