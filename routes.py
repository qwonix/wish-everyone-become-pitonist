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


def base_page(extra: dict):
    return {**dict(
        year=datetime.now().year,
    ), **extra}


@route('/')
@view('index')
def index():
    return base_page(dict(
        title='Главная',
        menu=menu(0),
    ))


@route('/forecast')
@view('forecast')
def forecast():
    return base_page(dict(
        title='Прогноз погоды',
        menu=menu(1),
    ))


@route('/conditions')
@view('conditions')
def conditions():
    return base_page(dict(
        title='Погодные явления',
        menu=menu(2),
    ))


@route('/instruments')
@view('instruments')
def instruments():
    return base_page(dict(
        title='Метеорология',
        menu=menu(3),
    ))
