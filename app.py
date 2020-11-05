from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def main_view():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def departures_view(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def tours_view(id):
    return render_template('tour.html')


@app.route('/about/')
def about():
    bracelet_data = {
        "Monday": {"steps": 35000, "calories": 2700, "laugh": 9},
        "Tuesday": {"steps": 10, "calories": 20500, "laugh": 100}
    }
    return render_template('about.html', bracelet_data=bracelet_data)

if __name__ == '__main__':
    app.run()
