import json
from json import JSONDecodeError

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'App is healthy'


@app.route('/users', methods=['GET'])
def getallusers():
    try:
        with open('data/data_v1.json') as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
        return {"File not found"}, 404
    except JSONDecodeError:
        return {"Invalid JSON"}, 400
    for person in data["people"]:
        person["prefix"] = person["email"].split("@")[0]
        person["domain"] = person["email"].split("@")[1]
    return jsonify(data)


if __name__ == '__main__':
    app.run()
