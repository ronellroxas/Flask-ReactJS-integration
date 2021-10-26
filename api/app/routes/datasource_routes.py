from flask import Blueprint
from app.controllers import datasource_controllers
datasource_bp = Blueprint("datasource_bp", __name__, url_prefix="/datasources")

datasource_bp.add_url_rule('/', view_func=datasource_controllers.index_page, methods=['GET'])