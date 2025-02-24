import sqlalchemy

from flask import Flask

from controllers.users import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix="/users")


@app.route('/')
def index():
    app.logger.info(f"SQL Alchemy v: {sqlalchemy.__version__}")
    return 'App is healthy'

if __name__ == '__main__':
    app.run(debug=True)

