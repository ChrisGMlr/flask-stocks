import os
import logging
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

class Config:
    LOG_LEVEL = logging.DEBUG
    LOG_FORMAT = '%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


def setup_logging():
    logging.basicConfig(level=Config.LOG_LEVEL, format=Config.LOG_FORMAT)
    return logging.getLogger(__name__)