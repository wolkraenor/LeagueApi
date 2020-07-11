import unittest
import app
from unittest.mock import patch
import json
from app.adapters.dragontail import Dragon
from tests.mocks.items import ITEMS


class TestItems(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.test_id = None

    @patch.object(Dragon, "get_items", return_value=ITEMS)
    def test_all_items(self, mock_items):
        response = self.client.get('/items')
        with open('tests/mocks/response/items.json') as json_response:
            expected_response = json.load(json_response)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(mock_items.is_called)
        self.assertTrue(response.json['data'][0] == expected_response['data'][0])

    @patch.object(Dragon, "get_items", return_value=ITEMS)
    def test_items_by_name(self, mock_items):
        response = self.client.get('/items/Boots of Speed')
        with open('tests/mocks/response/items_Boots_of_Speed.json') as json_response:
            expected_response = json.load(json_response)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(mock_items.is_called)
        self.assertTrue(response.json == expected_response)