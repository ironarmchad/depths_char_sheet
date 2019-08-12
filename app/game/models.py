from app import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, index=True)
    st_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    active = db.Column(db.Boolean, nullable=False)
    lore = db.Column(db.String)

    @classmethod
    def create_game(cls, game_name, st_id, game_lore, active=True):
        game = cls(name=game_name, st_id=st_id, lore=game_lore, active=active)
        db.session.add(game)
        db.session.commit()
        return game


