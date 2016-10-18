from flask import render_template, redirect, url_for

from . import app
from .forms import InitialSearchForm


@app.route('/', methods=('GET', 'POST'))
def index():
    form = InitialSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('trial'))

    return render_template('index.html', form=form)


@app.route('/trial')
def trial():
    return render_template('trial.html')
