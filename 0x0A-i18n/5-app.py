#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """Before the request"""
    user = get_user()
    g.user = user


def get_user():
    """get_user"""
    id = request.args.get('login_as')
    if id is None:
        return None
    try:
        return users.get(int(id))
    except ValueError:
        return None


@babel.localeselector
def get_locale():
    """Returns the best matched locale based on the languages
    requested by the client"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match('LANGUAGES')


@app.route('/')
def index():
    """basic index"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
