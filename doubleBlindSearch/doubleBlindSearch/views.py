from flask import render_template, redirect, request, url_for

from . import app
from .helpers import defaultFields, updateMeansLabelsAndFields


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html', **defaultFields)


@app.route('/trial', methods=('POST',))
def trial():
    data = request.form.to_dict(flat=True)
    query = data['query']

    # If form is valid
    if float(data['valueA']) != 0.0:
        # Process form
        data = updateMeansLabelsAndFields(data)
    else:
        # Display default field values
        data = defaultFields

    return render_template('trial.html', query=query, **data)
