from app import create_app, db
from app.auth.models import User


def prod_run(environ, start_response):
    char_app = create_app('prod')
    with char_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='su_ironarmchad').first():
            User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')

    char_app.run()


if __name__ == '__main__':
    char_app = create_app('prod')
    with char_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='su_ironarmchad').first():
            User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')

    char_app.run()
