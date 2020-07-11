import unittest
import app
from unittest.mock import patch
import json
from app.adapters.dragontail import Dragon
from tests.mocks.champions import CHAMPIONS


class TestChampions(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.test_id = None

    @patch.object(Dragon, "get_champions", return_value=CHAMPIONS)
    def test_all_champions(self, mock_champions):
        response = self.client.get('/champions')
        with open('tests/mocks/response/champions.json') as json_response:
            expected_response = json.load(json_response)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(mock_champions.is_called)
        self.assertTrue(response.json == expected_response)

    @patch.object(Dragon, "get_champions", return_value=CHAMPIONS)
    def test_champions_by_name(self, mock_champion):
        response = self.client.get('/champions/Aatrox')
        with open('tests/mocks/response/champion_Aatrox.json') as json_response:
            expected_response = json.load(json_response)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(mock_champion.is_called)
        self.assertTrue(response.json == expected_response)