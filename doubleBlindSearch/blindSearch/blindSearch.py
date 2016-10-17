from flask import Flask, request, render_template, redirect, url_for

from searchResults import yahoo, google, bing


app = Flask(__name__)


@app.route("/")
def landing():
    return render_template('landing.html')


@app.route('/search')
def search():
    query = request.args.get('q', False)
    if not query:
        return redirect(url_for('landing'))

    data = {
        'query': query,
        'engines': [
            {'name': 'Bing'  , 'links': bing(query)},
            {'name': 'Google', 'links': google(query)},
            {'name': 'Yahoo' , 'links': yahoo(query)},
        ],
    }
    return render_template('search.html', **data)


@app.route('/trial')
def trial():
    query = request.args.get('q', False)
    if not query:
        return redirect(url_for('landing'))

    return render_template('trial.html', query=query)


if __name__ == "__main__":
    app.run(debug=True)
