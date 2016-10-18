from flask import render_template

from . import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/trial')
def trial():
    return render_template('trial.html')
