from flask import render_template, redirect, request, url_for

from . import app
from .helpers import defaultFields


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html', **defaultFields)


@app.route('/trial', methods=('POST',))
def trial():
    data = request.form.to_dict(flat=True)

    return render_template('trial.html', **data)
