from app.application import app
from services.champions import ChampionsService
from flask import jsonify


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