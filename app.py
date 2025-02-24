import sqlalchemy

from flask import Flask
from config import Config, db,setup_logging
from data.users import init_db

logger = setup_logging()
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
init_db(app)

from controllers.users import user_bp
app.register_blueprint(user_bp, url_prefix="/users")


@app.route('/')
def index():
    logger.info(f"SQL Alchemy v: {sqlalchemy.__version__}")
    return 'App is healthy'

if __name__ == '__main__':
    app.run(debug=True)

