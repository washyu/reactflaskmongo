import time

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from pymongo import MongoClient

app = Flask(__name__, static_folder="../build", static_url_path="/")

app.config["MONGODB_SETTINGS"] = {
    "db": "animal_db",
    "host": "test_monogodb",
    "port": 27017,
    "username": "root",
    "password": "pass",
}
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)


class Animal(db.Document):
    meta = {"collection": "animal_tb"}
    myid = db.IntField(db_field="id", unique=True)
    name = db.StringField()
    type = db.StringField()


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file("index.html")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/time")
def get_current_time():
    return {"time": time.time()}


def get_db():
    client = MongoClient(
        host="test_monogodb",
        port=27017,
        username="root",
        password="pass",
        authSource="admin",
    )
    db = client["animal_db"]
    return db


@app.route("/api/animals")
def get_stored_animals():
    return jsonify({"animals": Animal.objects})
