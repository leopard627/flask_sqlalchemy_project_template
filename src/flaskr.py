
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MyNewPass@localhost/local_test'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 시크릿키를 입력하지 않으면 JWT 오류발생
app.config['SECRET_KEY'] = 'super-secret'

# flask-sqlalchemy + flask-migrate
db = SQLAlchemy(app)
# flask-migrate
migrate = Migrate(app, db)
# from src.models import User
# import models

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # mobile = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(220), nullable=False)

    # def __repr__(self):
        # return '<User %r>' % self.username

    def __str__(self):
        return "User(id='%s')" % self.id

def authenticate(username, password):
    user = User.query.filter(
            User.username==username,
            User.password==password).one()

    return user

def identity(payload):
    user_id = payload['identity']
    user = session.query(User).get(user_id)
    return user.id

jwt = JWT(app, authenticate, identity)

@app.route('/protected', methods=['GET'])
@jwt_required()
def hello_jwt():
    return jsonify({
        'message': 'hello world!'
    })

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'message': 'hello world!'
    })

if __name__ == "__main__":
    app.run()
