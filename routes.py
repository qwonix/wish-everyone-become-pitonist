"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@view('index')
def home():
    return dict(
        title='Главная',
        year=datetime.now().year,
    )

@route('/forecast')
@view('forecast')
def forecast():
    return dict(
        title='Прогноз погоды',
        year=datetime.now().year
    )

@route('/conditions')
@view('conditions')
def conditions():
    return dict(
        title='Погодные явления',
        year=datetime.now().year
    )

@route('/instruments')
@view('instruments')
def instruments():
    return dict(
        title='Метеорология',
        year=datetime.now().year
    )
