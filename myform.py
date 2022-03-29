from bottle import post, request
from re import compile as regex_compile


@post('/form', method='post')
def my_form():
    email = request.forms.get('email')
    question = request.forms.get('question')

    pattern = regex_compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    if not pattern.match(email):
        return f"Ошибка: email не соответствует шаблону"
    elif question == "":
        return f"Ошибка: введите ваш вопрос"

    return f"Спасибо! Ответ будет отправлен на почту: {email}!"
