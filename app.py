import os

import sqlalchemy
from sqlalchemy import create_engine, MetaData, select
import logging

from flask import Flask, jsonify, request
from flask.cli import load_dotenv
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.automap import automap_base

from utils import return_user

load_dotenv()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)

#Data base connection and ORM mapping
db_connection = os.getenv("db_connection")
engine = create_engine(db_connection, echo=True)
metadata_obj = MetaData()

metadata_obj.reflect(engine, only=['users', 'portfolio'])

Base = automap_base(metadata = metadata_obj)
Base.prepare()
schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}
@app.route('/')
def index():
    app.logger.info(f"SQL Alchemy v: {sqlalchemy.__version__}")
    return 'App is healthy'


@app.route('/users', methods=['GET'])
def getallusers():
    app.logger.info("Trying to get all users")
    user = Base.classes.users
    with engine.connect() as conn:
        result = conn.execute(select(user))
        user_list = return_user(result)

    return jsonify(user_list)

@app.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    app.logger.info(f"Trying to get user with id: {user_id}")
    user = Base.classes.users
    with engine.connect() as conn:
        result = conn.execute(select(user).where(user.user_id == user_id))
        user_list = return_user(result)

    return jsonify(user_list)

@app.route('/users/', methods = ['POST'])
#@expects_json(schema)
def add_new_user():
    data = request.get_json()
    user = Base.classes.users
    with engine.connect() as conn:
        conn.execute(insert(user).values(data))
        conn.commit()
    return jsonify(isError = False, message = "User added successfully", statusCode = 200)
if __name__ == '__main__':
    app.run(debug=True)

