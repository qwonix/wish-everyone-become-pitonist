from bottle import route, post, request, redirect
from re import compile as regex_compile
from os.path import dirname
import config as cfg1
import config2 as cfg2
import routes
from datetime import datetime


# import pdb

# функция для проверки почты
def is_valid_email(email: str) -> bool:
    email_pattern = regex_compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    return bool(email_pattern.match(email))


# функция для проверки заголовка
def is_valid_title(title: str) -> bool:
    return title != "" and len(title) <= 40


# функция для проверки описания
def is_valid_description(description: str) -> bool:
    return description != "" and len(description) <= 1000


# функция для проверки никнейма
def is_valid_nickname(nickname: str) -> bool:
    nickname_pattern = regex_compile(r"^\w{3,16}$")
    return bool(nickname_pattern.match(nickname))


# обработчик post запроса на маршруте /home
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


# функция для проверки почты, никнейма, заголовка и описания перед публикацией
def validate_all(email, nickname, title, description):
    error = ""

    if not is_valid_email(email):
        error = "email не соответствует шаблону"
    elif not is_valid_nickname(nickname):
        error = "никнейм должен состоять только из латинских символов/цифр и быть не длинее 16 символов"
    elif not is_valid_title(title):
        error = "некорректный заголовок, вы не можете использовать более 100 символов"
    elif not is_valid_description(description):
        error = "некорректный текст, вы не можете использовать более 1000 символов"

    if error != "":
        return f"Ошибка: {error}"

    return None


# json api для проверки данных от клиента
@route('/check_noveltie', method='post')
def check_noveltie():
    from json import dumps as json_dumps, loads as json_loads

    data = request.body.getvalue().decode('utf-8')
    data = json_loads(data)

    email = data['email']
    nickname = data['nickname']
    title = data['title']
    description = data['description']

    ret = validate_all(email, nickname, title, description)
    if ret is not None:
        return json_dumps({'error': ret})

    return json_dumps({'status': 'ok'})


# обработчик post запроса на маршруте /novelties
@post('/novelties', method='post')
def my_form1():
    email = request.params.email
    nickname = request.params.nickname
    title = request.params.title
    description = request.params.description

    ret = validate_all(email, nickname, title, description)
    if ret is not None:
        return ret

    novelties = routes.Noveltie(title, description, nickname, email, datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    config = cfg2.Config(dirname(__file__), "actual_novelties.json")
    config.data.append(novelties.to_dict())
    config.save()

    return redirect('/novelties')
