"""
Routes and views for the bottle application.
"""

from bottle import route, view, post, request, template
from datetime import datetime


class MenuOption:
    name: str
    link: str
    is_active: bool

    def __init__(self, name: str, link: str, is_active: bool = False):
        self.name = name
        self.link = link
        self.is_active = is_active

    def class_name(self):
        name = "nav-link"
        if self.is_active:
            name += " active"
        return name


def menu(idx=None):
    options = [MenuOption('На главную', '/'),
               MenuOption('Прогноз погоды', '/forecast'),
               MenuOption('Погодные явления', '/conditions'),
               MenuOption('Метеорология', '/instruments'),
               MenuOption('Форма', '/form'),
               MenuOption('Комментарии', '/comments')]

    if idx is not None:
        options[idx].is_active = True

    return options


class WeatherForecast:
    title: str
    description: str
    image_link: str
    date: str

    def __init__(self, title: str, description: str, image_link: str, date: str):
        self.title = title
        self.description = description
        self.image_link = image_link
        self.date = date


class WeatherCondition:
    name: str
    description: str
    image_link: str

    def __init__(self, name: str, description: str, image_link: str):
        self.name = name
        self.description = description
        self.image_link = image_link


def base_page(extra: dict):
    return {**dict(year=datetime.now().year, ), **extra}


@route('/')
@view('index')
def index():
    return base_page(dict(title='Главная',
                          menu=menu(0), ))


@route('/forecast')
@view('forecast')
def forecast():
    return base_page(dict(title='Прогноз погоды',
                          menu=menu(1),
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
                                                            'Послезавтра')], ))


@route('/conditions')
@view('conditions')
def conditions():
    return base_page(dict(title='Погодные явления',
                          menu=menu(2),
                          weather_conditions=[WeatherCondition('Снег',
                                                               'форма атмосферных осадков, состоящая из мелких кристаллов льда',
                                                               'https://i.imgur.com/OzK5hGp.png', ),
                                              WeatherCondition('Дождь',
                                                               'атмосферные осадки, выпадающие из облаков в виде капель жидкости',
                                                               'https://i.imgur.com/1LVyrKM.png', ),
                                              WeatherCondition('Град',
                                                               'вид ливневых осадков в виде частиц льда преимущественно округлой формы',
                                                               'https://i.imgur.com/WjQk3kB.png', ),
                                              WeatherCondition('Гроза',
                                                               'атмосферное явление, при котором возникают электрические разряды',
                                                               'https://i.imgur.com/CHUnsl8.png', ),
                                              WeatherCondition('Смерч',
                                                               'атмосферный вихрь, возникающий в грозовом облаке',
                                                               'https://i.imgur.com/GEMdGLR.png', ),
                                              WeatherCondition('Туман',
                                                               'атмосферное явление, скопление воды в воздухе',
                                                               'https://i.imgur.com/7F9HA77.png', ), ], ))


@route('/instruments')
@view('instruments')
def instruments():
    return base_page(dict(title='Метеорология',
                          menu=menu(3), ))
