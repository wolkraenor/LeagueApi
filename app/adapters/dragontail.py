import requests
import json
from app.settings import API_URL


class Dragon():
    def get_champions(self):
        url = API_URL + 'en_US/champion.json'
        try:
            response = requests.get(url)
            return json.loads(response.text)
        except:
            raise Exception

    def get_items(self):
        url = API_URL + 'en_US/item.json'
        response = requests.get(url)
        return json.loads(response.text)