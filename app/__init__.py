from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.settings import (APP_NAME, APP_VERSION, DEBUG, MYSQL_BASE, MYSQL_HOST,
                          MYSQL_PASSWORD, MYSQL_USER)
from app.services.champions import ChampionsService
from app.services.items import ItemsService
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from . import routes


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
