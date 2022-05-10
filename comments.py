from bottle import route, view, post, request, redirect
from datetime import datetime
from routes import base_page, menu, WeatherForecast
from re import compile as regex_compile
from os.path import exists as file_exists, join as path_join, dirname
from json import dumps as json_dumps, load as json_loads


def isCorrectPhone(phone: str):
    pattern = regex_compile(r"^\+7\ \d{3}\ \d{3}-\d{2}-\d{2}$")
    if pattern.match(phone):
        return True
    else:
        return False


def isCorrectName(name: str):
    pattern = regex_compile(r"^[А-Яа-яЁё]{3,}$")
    if pattern.match(name):
        return True
    else:
        return False


class Comment:
    name: str
    text: str
    phone: str
    date: str

    def __init__(self, name: str, text: str, phone: str, date: str):
        self.name = name
        self.text = text
        self.phone = phone
        self.date = date

    def to_dict(self):
        return {'name': self.name,
                'text': self.text,
                'phone': self.phone,
                'date': self.date}

    @staticmethod
    def from_dict(d: dict):
        return Comment(d['name'], d['text'], d['phone'], d['date'])


@post('/comments', method='post')
def my_form():
    name = request.params.name
    text = request.params.text
    phone = request.params.phone

    if not isCorrectPhone(phone) or not isCorrectName(name):
        return

    comment = Comment(name, text, phone, datetime.now().strftime("%d %B, %Y %H:%M"))

    full_filename = path_join(dirname(__file__), "comments.json")
    if not file_exists(full_filename):
        open(full_filename, "w+").write(json_dumps([]))

    data = json_loads(open(full_filename, "r+"))

    data.insert(0, comment.to_dict())
    open(full_filename, "w+").write(json_dumps(data, indent=4))

    redirect('/comments')


@route('/comments')
@view('comments')
def comments():
    full_filename = path_join(dirname(__file__), "comments.json")
    if not file_exists(full_filename):
        open(full_filename, "w+").write(json_dumps([]))

    data = json_loads(open(full_filename, "r+"))

    comments = []
    for c in data:
        comments.append(Comment.from_dict(c))

    return base_page(dict(title='Прогноз погоды',
                          menu=menu(5),
                          weather_forecast=[WeatherForecast('+2',
                                                            'Облачно',
                                                            'https://i.imgur.com/7GTBjlM.png',
                                                            'Сегодня'),
                                            WeatherForecast('+5',
                                                            'Ясно',
                                                            'https://i.imgur.com/t3XGTHL.png',
                                                            'Завтра'),
                                            WeatherForecast('0',
                                                            'Дождь',
                                                            'https://i.imgur.com/9gufmFS.png',
                                                            'Послезавтра')],
                          comments=comments))
