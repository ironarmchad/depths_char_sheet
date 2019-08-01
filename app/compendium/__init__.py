from flask import Blueprint

compend = Blueprint('compend', __name__, template_folder='templates')

from app.compendium import routes