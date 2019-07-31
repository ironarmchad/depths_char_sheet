from app.character import main
from flask import render_template


@main.route('/')
def home_page():
    print('it is routing')
    return render_template('home.html')
