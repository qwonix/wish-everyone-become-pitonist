"""
Routes and views for the bottle application.
"""

from bottle import route, view
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
    options = [
        MenuOption('На главную', '/'),
        MenuOption('Прогноз погоды', '/forecast'),
        MenuOption('Погодные явления', '/conditions'),
        MenuOption('Метеорология', '/instruments'),
    ]

    if idx is not None:
        options[idx].is_active = True

    return options


@route('/')
@view('index')
def index():
    return dict(
        title='Главная',
        menu=menu(0),
        year=datetime.now().year,
    )


@route('/forecast')
@view('forecast')
def forecast():
    return dict(
        title='Прогноз погоды',
        menu=menu(1),
        year=datetime.now().year,
    )


@route('/conditions')
@view('conditions')
def conditions():
    return dict(
        title='Погодные явления',
        menu=menu(2),
        year=datetime.now().year,
    )


@route('/instruments')
@view('instruments')
def instruments():
    return dict(
        title='Метеорология',
        menu=menu(3),
        year=datetime.now().year,
    )
