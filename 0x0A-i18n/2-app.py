#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from babel import negotiate_locale

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Config Class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """basic index"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """Returns the best matched locale based on the languages
    requested by the client"""
    return negotiate_locale('LANGUAGES',
                            request.accept_languages.best_match(
                                app.config['LANGUAGES']))


if __name__ == '__main__':
    app.run(debug=True)
