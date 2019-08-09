from app import create_app, db
from app.auth.models import User
import sys


if __name__ == '__main__':
    char_app = create_app('prod')
    with char_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='su_ironarmchad').first():
            User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')

    char_app.run()

else:
    char_app = create_app('prod')
    sys.stderr.write('check 1\n')
    with char_app.app_context():
        sys.stderr.write('check 2\n')
        db.create_all()
        sys.stderr.write('check 3\n')
        if not User.query.filter_by(user_name='su_ironarmchad').first():
            sys.stderr.write('check 4\n')
            User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')
    sys.stderr.write('check 5\n')

    char_app.run()
    sys.stderr.write('check 6\n')
