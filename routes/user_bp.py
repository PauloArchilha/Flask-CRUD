from flask import Blueprint
from controllers.user_controller import index, store, update, show, delete


user_bp = Blueprint(name="user_bp", import_name=__name__)

user_bp.route(rule="/", methods=['GET'])(index)
user_bp.route(rule="/criar", methods=['POST'])(store)
user_bp.route(rule="/alterar/<int:user_id>", methods=['PUT'])(update)
user_bp.route(rule="/<int:user_id>", methods=['GET'])(show)
user_bp.route(rule="/<int:user_id>", methods=['DELETE'])(delete)
