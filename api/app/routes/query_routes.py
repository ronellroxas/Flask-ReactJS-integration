from flask import Blueprint
from app.controllers import query_controllers

query_bp = Blueprint("query_bp", __name__, url_prefix="/query")

query_bp.add_url_rule('/', view_func=query_controllers.index_page, methods=['GET'])

query_bp.add_url_rule('/init', view_func=query_controllers.init_data, methods=['GET'])