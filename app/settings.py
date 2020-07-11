import os

API_URL = os.environ.get("API_URL", "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/")
TOKEN = os.environ.get("TOKEN")
DEBUG = os.environ.get('DEBUG', False)
APP_NAME = os.environ.get('APP_NAME', 'LeagueApi')
APP_VERSION = os.environ.get('APP_VERSION', 'v.0.1')
APP_PORT = os.environ.get('APP_PORT', 80)
