import os
import flask
import sqlite3
from time import sleep
from celery import Celery
from flask import jsonify, make_response, request
from init_db import createDb
from tasks import updateResult

if os.path.isfile('test.sqlite'):
      pass
else:
    createDb()

connection = sqlite3.connect('test.sqlite', check_same_thread=False, timeout=10, isolation_level=None)
cursor = connection.cursor()

# Flask app below

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'




@app.route('/', methods=['GET'])
def home():
    return make_response(jsonify("Hi from test API"), 200)


@app.route('/calculate/<number1>/<number2>', methods=['POST'])
def calc_numbers(number1, number2):
    number1, number2 = request.view_args['number1'], request.view_args['number2']
    data = cursor.execute("INSERT INTO sums (number1, number2)VALUES (?, ?)", (number1, number2))
    updateResult.delay(id=data.lastrowid, number1=int(number1),number2=int(number2))
    return make_response(jsonify({"id":data.lastrowid}), 200)



@app.route('/get_answer/<id>/', methods=['GET'])
def get_sum_by_id(id):
    data = cursor.execute("SELECT * FROM sums WHERE id = ?", (id,)).fetchone()
    if not data:
        return make_response(jsonify({"error": f"No data found with id: {id}"}), 404)
    if data and data[3] is None:
        return make_response(jsonify({"message": "Please wait..."}), 200)
    return make_response(jsonify({"sum":data[3]}), 200)


app.run()