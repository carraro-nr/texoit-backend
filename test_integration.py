import unittest
from app import app, db
from models import Movie

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
        Movie.load_data('movies.csv')

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_producers_intervals(self):
        response = self.app.get('/producers/intervals')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('min', data)
        self.assertIn('max', data)

if __name__ == '__main__':
    unittest.main()
