
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MyNewPass@localhost/local_test'

# flask-sqlalchemy + flask-migrate
db = SQLAlchemy(app)
# flask-migrate
migrate = Migrate(app, db)
# from src.models import User
# import models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # mobile = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(220), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 'hello world!'
    })

if __name__ == "__main__":
    app.run()
