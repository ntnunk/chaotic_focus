from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
app.config['SECRET_KEY'] = '87a957be5fb7c996ac2b927d5c4fb97f'

db = SQLAlchemy(app)

from ChaoticFocus import routes
