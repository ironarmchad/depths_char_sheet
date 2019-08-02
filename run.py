from app import create_app, db
from app.auth.models import User

if __name__ == "__main__":
    char_app = create_app('dev')
    with char_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='su_ironarmchad').first():
            User.create_user(user='su_ironarmchad',
                             password='PIANO@230jap',
                             role='SUPER')

    char_app.run()
