from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NHL(db.Model):
    __tablename__ = 'Varžybos'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    komanda_1 = db.Column(db.String)
    komanda_2 = db.Column(db.String)
    taškai_1 = db.Column(db.Integer)
    taškai_2 = db.Column(db.Integer)

