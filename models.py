from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    studios = db.Column(db.String, nullable=False)
    producers = db.Column(db.String, nullable=False)
    winner = db.Column(db.Boolean, nullable=False)

    @staticmethod
    def load_data(file_path):
        import csv
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                movie = Movie(
                    year=int(row['year']),
                    title=row['title'],
                    studios=row['studios'],
                    producers=row['producers'],
                    winner=(row['winner'].lower() == 'yes')
                )
                db.session.add(movie)
            db.session.commit()
