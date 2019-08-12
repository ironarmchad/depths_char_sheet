from flask import Blueprint

game_pages = Blueprint('game', __name__, template_folder='templates')

from app.game import routes