import os
from sqlalchemy import MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'user.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context()
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

from website import routes
