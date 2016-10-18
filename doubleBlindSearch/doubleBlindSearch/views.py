from flask import render_template, redirect, request, url_for

from . import app
from .helpers import defaultFields


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html')


@app.route('/trial', methods=('POST',))
def trial():

    return render_template('trial.html')
