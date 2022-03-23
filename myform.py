from bottle import post, request
from re import compile as regex_compile


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
        return f"Thanks! The answer will be sent to the mail {email}"
