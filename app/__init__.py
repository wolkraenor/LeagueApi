from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy  
from app.settings import (APP_NAME, APP_VERSION, DEBUG, MYSQL_BASE, MYSQL_HOST,
                          MYSQL_PASSWORD, MYSQL_USER) 
from app.services.champions import ChampionsService
from app.services.items import ItemsService


app = Flask(__name__)
app.debug = DEBUG
db = SQLAlchemy()


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{u}:{p}@{h}/{db}'.format(u=MYSQL_USER,
                                                                          p=MYSQL_PASSWORD,
                                                                          h=MYSQL_HOST,
                                                                          db=MYSQL_BASE)
                                        

migrate = Migrate(app, db)
manager = Manager(app)
db.init(app)
manager.add_command('db', MigrateCommand)


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