from config import db



def init_db(app):
    with app.app_context():
        class User(db.Model):
            __table__ = db.Table("users", db.metadata, autoload_with=db.engine)

        globals().update({"User": User})

User = None