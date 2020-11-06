from flask import Flask, render_template, abort

from numpy import random

import data

app = Flask(__name__)


@app.route('/')
def main_view():
    a = [int(i) for i in range(1, len(data.tours) + 1)]
    list_for_random = random.choice(a, 6, replace=False)
    tours_for_main = dict()
    for i in list_for_random:
        tours_for_main[i] = data.tours[i]
    return render_template('index.html', tours=tours_for_main, departures=data.departures)


@app.route('/departures/<departure>/')
def departures_view(departure):
    if departure in data.departures:
        dep_tours = dict()
        for key, val in data.tours.items():
            if val["departure"] == departure:
                dep_tours[key] = val
        n = len(dep_tours)
        t = 'тур' + ('ов' if n % 10 == 0 or 4 < n % 10 < 10 or 10 < n % 100 < 15 else 'а' if 1 < n % 10 < 5 else '')
        return render_template('departure.html', departure=departure, tours=dep_tours, departures=data.departures, t=t)
    else:
        abort(404)


@app.route('/tours/<int:tour_id>/')
def tours_view(tour_id):
    tour = data.tours.get(tour_id)
    if tour is None:
        abort(404)
    stars = int(tour['stars']) * '★'
    return render_template('tour.html', id=tour_id, tour=tour, departures=data.departures, stars=stars)


@app.route('/departures/')
@app.route('/tours/')
def all_view():
    return render_template('all_tours.html', departures=data.departures, tours=data.tours)


@app.route('/sales/')
def sales_view():
    return render_template('sales.html')


@app.errorhandler(404)
def render_not_found(error):
    return render_template('404_page.html')


if __name__ == '__main__':
    app.run()
