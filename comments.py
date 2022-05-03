from bottle import route, view, post, request, redirect, template, static_file

from datetime import datetime
from routes import base_page, menu, WeatherForecast

from os.path import exists as file_exists, join as path_join, dirname
from json import dumps as json_dumps, load as json_loads


class Config:
    filename: str
    data: list = []

    def __init__(self, working_directory: str, file: str):
        filename = path_join(working_directory, file)
        if not file_exists(filename):
            open(filename, "w+").write(json_dumps([]))

        self.filename = filename
        self.data = json_loads(open(filename, "r+"))

    def save(self):
        open(self.filename, "w+").write(json_dumps(self.data, indent=4))


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
    name = request.forms.get('name')
    text = request.forms.get('text')
    phone = request.forms.get('phone')

    comment = Comment(name, text, phone, datetime.now().strftime("%d %B, %Y %H:%M"))

    config = Config(dirname(__file__), "json_comments.json")
    config.data.append(comment.to_dict())
    config.save()

    redirect('/comments')


@route('/comments')
@view('comments')
def comments():
    comments = []

    config = Config(dirname(__file__), "json_comments.json")
    for c in config.data:
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
