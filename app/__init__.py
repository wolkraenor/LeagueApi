from flask import Flask, request, jsonify, render_template
from app.settings import APP_NAME, APP_VERSION, DEBUG
from app.services.champions import ChampionsService
from app.services.items import ItemsService

app = Flask(__name__)
app.debug = DEBUG

@app.route("/")
def index():
    return {
        "app": APP_NAME,
        "version": APP_VERSION
    }

@app.route("/champions", methods=['GET'])
def all_champions():
    champions = ChampionsService()
    data = champions.store()
    return jsonify(champions=data)

@app.route("/champions/<name>", methods=['GET'])
def champions_by_name(name):
    champions = ChampionsService()
    data = champions.champion_data(name=name)
    return jsonify(data=data)

@app.route("/items", methods=['GET'])
def all_items():
    items = ItemsService()
    data = items.store()
    return jsonify(data=data)

@app.route("/items/<name>", methods=['GET'])
def items_by_name(name):
    items = ItemsService()
    data = items.item_by_name(name=name)
    return jsonify(data=data)