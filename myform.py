from bottle import post, request
from re import compile as regex_compile
from os.path import dirname
from config import Config
# import pdb


@post('/home', method='post')
def my_form():
    email = request.forms.get('email')
    question = request.forms.get('question')

    pattern = regex_compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    error = ""

    if not pattern.match(email):
        error = "email не соответствует шаблону"
    elif question == "":
        error = "введите ваш вопрос"

    if error != "":
        return f"Ошибка: {error}"
    else:
        # pdb.set_trace()
        config = Config(dirname(__file__), "questions.json")
        if config.exists(email):
            questions = config.try_get(email)
            questions.append(question)
            config.set(email, questions)
        else:
            config.set(email, [question])
        config.save()
        return f"Thanks! The answer will be sent to the mail {email}"
