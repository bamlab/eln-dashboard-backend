from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello():
    with open('trade_flow_DC.json') as json_data:
        d = json.load(json_data)
        print(d)
        resp = jsonify(d)
        resp.status_code = 200

        return resp
