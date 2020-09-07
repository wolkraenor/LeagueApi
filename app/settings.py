import os

API_URL = os.environ.get("API_URL", "http://ddragon.leagueoflegends.com/cdn/10.14.1/data/")
TOKEN = os.environ.get("TOKEN")
DEBUG = os.environ.get('DEBUG', False)
APP_NAME = os.environ.get('APP_NAME', 'LeagueApi')
APP_VERSION = os.environ.get('APP_VERSION', 'v.0.1')
APP_PORT = os.environ.get('APP_PORT', 80)
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_BASE = os.environ.get('MYSQL_BASE')
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_ENGINE = os.environ.get('MYSQL_ENGINE')
MYSQL_PORT = os.enviroment.get('MYSQL_PORT')