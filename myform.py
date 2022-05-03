from bottle import route, post, request, redirect
from re import compile as regex_compile
from os.path import dirname
import config as cfg1
import config2 as cfg2
import routes
from datetime import datetime


# import pdb

def is_valid_email(email: str) -> bool:
    email_pattern = regex_compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    return bool(email_pattern.match(email))


def is_valid_title(title: str) -> bool:
    return title != "" and len(title) <= 32


def is_valid_description(description: str) -> bool:
    return description != "" and len(description) <= 1000


def is_valid_nickname(nickname: str) -> bool:
    nickname_pattern = regex_compile(r"^\w{3,16}$")
    return bool(nickname_pattern.match(nickname))


@post('/home', method='post')
def my_form():
    email = request.forms.get('email')
    question = request.forms.get('question')

    error = ""

    if not is_valid_email(email):
        error = "email не соответствует шаблону"
    elif question == "":
        error = "введите ваш вопрос"

    if error != "":
        return f"Ошибка: {error}"
    else:
        # pdb.set_trace()
        config = cfg1.Config(dirname(__file__), "questions.json")
        if config.exists(email):
            questions = config.try_get(email)
            questions.append(question)
            config.set(email, questions)
        else:
            config.set(email, [question])
        config.save()
        return f"Thanks! The answer will be sent to the mail {email}"


def validate_all(email, nickname, title, description):
    error = ""

    if not is_valid_email(email):
        error = "email не соответствует шаблону"
    elif not is_valid_nickname(nickname):
        error = "nickname должен состоять только из латинских символов/цифр и быть не длинее 16 символов"
    elif not is_valid_title(title):
        error = "некорректный заголовок"
    elif not is_valid_description(description):
        error = "некорректный текст"

    if error != "":
        return f"Ошибка: {error}"

    return None


@route('/check_noveltie/data=:data')
def check_noveltie(data):
    from json import dumps as json_dumps, loads as json_loads

    data = json_loads(data)

    email = data['email']
    nickname = data['nickname']
    title = data['title']
    description = data['description']

    ret = validate_all(email, nickname, title, description)
    if ret is not None:
        return json_dumps({'error': ret})

    return json_dumps({'status': 'ok'})


@post('/novelties', method='post')
def my_form1():
    email = request.forms.get('email')
    nickname = request.forms.get('nickname')
    title = request.forms.get('title')
    description = request.forms.get('description')

    ret = validate_all(email, nickname, title, description)
    if ret is not None:
        return ret

    novelties = routes.Noveltie(title, description, nickname, email, datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    config = cfg2.Config(dirname(__file__), "actual_novelties.json")
    config.data.append(novelties.to_dict())
    config.save()

    return redirect('/novelties')
