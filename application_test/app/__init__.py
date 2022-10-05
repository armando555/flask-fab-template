import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from app.security.sqla import SecurityManager
from app.custom_views.index import MyIndexView
from flask_migrate import Migrate
from flask_cors import CORS
import click
from flask.cli import with_appcontext
import redis

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
cache_redis = redis.Redis(host=app.config["REDIS_HOST"],port=6379)
db = SQLA(app)
cors = CORS(app)
migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session, security_manager_class=SecurityManager,indexview=MyIndexView)

# create command function
@click.command(name='seed_db')
@with_appcontext
def seed_db():
    models.set_db_defaults(appbuilder.get_session)
 
# add command function to cli commands
app.cli.add_command(seed_db)

from . import views
from . import models

from . import api