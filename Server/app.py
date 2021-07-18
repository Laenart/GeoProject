from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)


@app.route('/ping', methods=['GET'])
@cross_origin(supports_credentials=True)
def ping_pong():
    return jsonify('pong!')


class geo_model(db.Model):
    __tablename__ = 'tGeo'

    Id = db.Column(db.Integer, primary_key=True)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    TypeId = db.Column(db.Integer)
    Distance = db.Column(db.Float)

    def __repr__(self):
        return f"<Geo {self.Id}: lat {self.Latitude}; lon {self.Longitude}>"
