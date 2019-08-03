from app import db, bcrypt
from flask_login import UserMixin, current_user
from app import login_manager
from functools import wraps


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True, index=True)
    user_password = db.Column(db.String(80))
    role = db.Column(db.String(10))

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    @classmethod
    def create_user(cls, user, password, role='BASIC'):
        user = cls(user_name=user,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'),
                   role=role)
        db.session.add(user)
        db.session.commit()
        return user

    def __repr__(self):
        return 'User {} is {} and is a {} user.'.format(self.id, self.user_name, self.role)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            if (current_user.role != role) and (role != "ANY") and (current_user.role != 'SUPER'):
                return login_manager.unauthorized()
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper
