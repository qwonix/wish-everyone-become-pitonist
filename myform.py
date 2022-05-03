from os.path import exists

from bottle import post, request, route, view
from re import compile as regex_compile
from routes import base_page, menu
import json


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
    if exists('json_question.json'):
        with open('json_question.json', 'r', encoding='utf-8') as read_json:
            questions = json.load(read_json)

    with open('json_question.json', 'w', encoding='utf-8') as write_json:
        if email in questions:
            questions.get(email).append(question)
        else:
            questions[email] = [question]
        json.dump(questions, write_json)

    return f"Спасибо! Ответ будет отправлен на почту: {email}!"
