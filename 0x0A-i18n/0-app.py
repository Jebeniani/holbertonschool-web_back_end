#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    """basic index"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
