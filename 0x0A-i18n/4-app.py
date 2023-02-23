#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, render_template, request, g
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
    return render_template('4-index.html')


def get_locale():
    """Returns the best matched locale based on the languages
    requested by the client"""
    if 'locale' in g:
        return g.locale

    locale = request.args.get('locale')
    if locale and locale in 'LANGUAGES':
        g.locale = locale
        return locale

    best_match = negotiate_locale(
        'LANGUAGES', request.accept_languages.best_match('LANGUAGES'))

    g.locale = best_match

    return best_match


if __name__ == '__main__':
    app.run(debug=True)
