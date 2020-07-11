import unittest
from app.__init__ import app
from tests.test_champions import TestChampions
from tests.test_items import TestItems


class Init(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.test_id = None

    def tearDown(self):
        self.app_context.pop()

    def test_404(self):
        response = self.client.get('/wrong/url')
        self.assertTrue(response.status_code == 404)

    def test_hi_200(self):
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)


Init()
TestChampions()
TestItems()
if __name__ == "__main__":
    unittest.main(warnings='ignore')

#pipenv run coverage run --source app tests/__init__.py
# pipenv run coverage report
# pipenv run coverage html
#open htmlcov/index.html
#pipenv run python tests/__init__.py