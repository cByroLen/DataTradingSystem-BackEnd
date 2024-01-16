from flask import Flask
from .extensions import init_extensions
from App.blueprints.user import bp as user_bp
from App.blueprints.data_asset import bp as data_asset_bp
from App.blueprints.data_products import bp as data_products_bp
from App.blueprints.tranction_contract import bp as tc_bp
from .models import *


def create_app():
    app = Flask(__name__)
    # 绑定配置文件
    app.config.from_pyfile('config.py')
    # 初始化
    init_extensions(app)
    # 注册蓝图
    app.register_blueprint(blueprint=user_bp)
    app.register_blueprint(blueprint=data_asset_bp)
    app.register_blueprint(blueprint=data_products_bp)
    app.register_blueprint(blueprint=tc_bp)

    return app

