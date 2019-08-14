from app import db


class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, index=True)
    st_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    active = db.Column(db.Boolean, nullable=False)
    lore = db.Column(db.String)
    summary = db.Column(db.String(150))

    @classmethod
    def create_game(cls, game_name, st_id, game_lore, game_summary, active=True):
        game = cls(name=game_name, st_id=st_id, lore=game_lore, summary=game_summary, active=active)
        db.session.add(game)
        db.session.commit()
        return game

    def __repr__(self):
        return '{} - {}'. format(self.id, self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name
