#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel

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
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """Returns the best matched locale based on the languages
    requested by the client"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match('LANGUAGES')


if __name__ == '__main__':
    app.run(debug=True)
