from flask import render_template, redirect, request, url_for

from . import app
from .helpers import defaultFields, updateMeansLabelsAndFields


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html', **defaultFields)


@app.route('/trial', methods=('POST',))
def trial():
    data = request.form.to_dict(flat=True)

    # If form is valid
    if float(data['valueA']) != 0.0:
        # Process form
        data = updateMeansLabelsAndFields(data)

    return render_template('trial.html', **data)
