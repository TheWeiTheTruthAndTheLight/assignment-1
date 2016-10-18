from flask import render_template, redirect, request, url_for

from . import app
from .forms import InitialSearchForm, TrialForm
from .helpers import defaultFields


@app.route('/', methods=('GET', 'POST'))
def index():
    form = InitialSearchForm(**defaultFields)
    if form.validate_on_submit():
        return redirect(url_for('trial'), code=307)

    return render_template('index.html', form=form)


@app.route('/trial', methods=('POST',))
def trial():
    form = TrialForm()

    # Advance to next trial (if form is valid)
    if form.validate_on_submit():
        return redirect('/success')

    return render_template('trial.html', form=form)
