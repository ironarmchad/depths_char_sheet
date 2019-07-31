from app import db, bcrypt
from flask_login import UserMixin
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True, index=True)
    user_password = db.Column(db.String(80))

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, password):
        user = cls(user_name=user,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()
        return user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
