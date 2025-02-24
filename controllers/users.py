import logging

from flask import  jsonify, request, Blueprint
from config import db
from data.users import User
from utils import return_user

user_bp = Blueprint('user', __name__)
logger = logging.getLogger(__name__)


@user_bp.get('/')
def getallusers():
    logger.info("Trying to get all users")
    user_list = db.session.query(User).all()
    return jsonify(return_user(user_list))

@user_bp.get('/<user_id>')
def get_single_user(user_id):
    logger.info(f"Trying to get user with id: {user_id}")
    result = db.session.query(User).filter(User.user_id == user_id).all()
    user_list = return_user(result)

    return jsonify(user_list)

@user_bp.post('/')
#@expects_json(schema)
def add_new_user():
    data = request.get_json()
    user = User(
        name = data.get("name"),
        email = data.get("email")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(isError = False, message = "User added successfully", statusCode = 200)