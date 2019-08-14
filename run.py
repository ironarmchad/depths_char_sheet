from app import create_app, db
from app.auth.models import User
from app.game.models import Game
import sys


if __name__ == '__main__':
    char_app = create_app('dev')
    with char_app.app_context():
        db.create_all()
        user = User.query.filter_by(user_name='su_ironarmchad').first()
        if not user:
            user = User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')
        if not Game.query.filter_by(name='No Game').first():
            Game.create_game(game_name='No Game', game_lore='', game_summary="", st_id=user.id)

    char_app.run()

else:
    char_app = create_app('prod')
    with char_app.app_context():
        db.create_all()
        user = User.query.filter_by(user_name='su_ironarmchad').first()
        if not user:
            user = User.create_user(user='su_ironarmchad',
                                    password='PIANO@230jap',
                                    role='SUPER')
        if not Game.query.filter_by(name='No Game').first():
            Game.create_game(game_name='No Game', game_lore='', game_summary="", st_id=user.id)

