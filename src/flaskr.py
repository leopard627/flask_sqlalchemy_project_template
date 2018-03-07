
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
from src.models import User

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
