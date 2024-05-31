from flask import Flask, jsonify
from models import db, Movie
from utils import calculate_intervals

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()
    Movie.load_data('movies.csv')

@app.route('/producers/intervals', methods=['GET'])
def get_producers_intervals():
    min_intervals, max_intervals = calculate_intervals()
    return jsonify({
        "min": min_intervals,
        "max": max_intervals
    })

if __name__ == '__main__':
    app.run(debug=True)
