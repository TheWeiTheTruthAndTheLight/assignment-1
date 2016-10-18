from flask import render_template, redirect, request, url_for

from . import app
from .forms import InitialSearchForm, TrialForm


@app.route('/', methods=('GET', 'POST'))
def index():
    form = InitialSearchForm()
    if form.validate_on_submit():
        return redirect(url_for('trial'), code=307)

    return render_template('index.html', form=form)


@app.route('/trial', methods=('POST',))
def trial():
    # Retrieve current query
    try:
        current_query = request.form['query']
    except KeyError:
        return redirect(url_for('index'))

    form = TrialForm()

    # Advance to next trial (if form is valid)
    if form.validate_on_submit():
        return redirect('/success')

    return render_template('trial.html', form=form, current_query=current_query)
