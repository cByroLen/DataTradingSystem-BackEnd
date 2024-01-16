# 拓展 避免循环引用
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
# cors = CORS()

def init_extensions(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)