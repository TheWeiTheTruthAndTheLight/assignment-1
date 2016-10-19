from flask import render_template, redirect, request, url_for

from . import app
from .helpers import defaultFields, searchAndCollect, updateMeansLabelsAndFields


@app.route('/', methods=('GET',))
def index():
    return render_template('index.html', **defaultFields)


@app.route('/trial', methods=('POST',))
def trial():
    fields = request.form.to_dict(flat=True)
    query = fields['query']
    scoreFormulaConstant = 1.15
    resultsCount = 5
    results = searchAndCollect(query, fields, resultsCount)

    # If form is valid
    if float(fields['valueA']) != 0.0:
        # Process form
        stats = updateMeansLabelsAndFields(fields, resultsCount, scoreFormulaConstant)
    else:
        # Display current field values
        stats = fields

    return render_template('trial.html', query=query, results=results, stats=stats)
