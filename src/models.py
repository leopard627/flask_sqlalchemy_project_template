from src.flaskr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # mobile = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(220), unique=True, nullable=False)


    __table_args__ = {'extend_existing': True}

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return "User(id='%s')" % self.id
