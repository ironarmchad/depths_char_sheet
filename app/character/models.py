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


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(20), nullable=False, index=True)
    char_type = db.Column(db.String(10), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('Game.id'))
    lore = db.Column(db.String)
    strength = db.Column(db.Integer, nullable=False)
    reflex = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    vitality = db.Column(db.Integer, nullable=False)
    awareness = db.Column(db.Integer, nullable=False)
    willpower = db.Column(db.Integer, nullable=False)
    imagination = db.Column(db.Integer, nullable=False)
    attunement = db.Column(db.Integer, nullable=False)
    faith = db.Column(db.Integer, nullable=False)
    luck = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    actions = db.Column(db.String)

    @classmethod
    def create_character(cls,
                         char_owner,
                         char_name,
                         char_lore,
                         char_strength,
                         char_reflex,
                         char_vitality,
                         char_speed,
                         char_awareness,
                         char_willpower,
                         char_imagination,
                         char_attunement,
                         char_faith,
                         char_luck,
                         char_charisma):
        character = cls(owner=char_owner,
                        name=char_name,
                        lore=char_lore,
                        strength=char_strength,
                        reflex=char_reflex,
                        vitality=char_vitality,
                        speed=char_speed,
                        awareness=char_awareness,
                        willpower=char_willpower,
                        imagination=char_imagination,
                        attunement=char_attunement,
                        faith=char_faith,
                        luck=char_luck,
                        charisma=char_charisma)
        db.session.add(character)
        db.session.commit()
        return character


class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)
    name = db.Column(db.String(30), index=True, nullable=False)
    act_type = db.Column(db.String(10), nullable=False)
    lore = db.Column(db.String)
    mechanics = db.Column(db.String)

    @classmethod
    def create_action(cls, char_id, name, act_type, lore, mechanics):
        action = cls(char_id=char_id,
                     name=name,
                     act_type=act_type,
                     lore=lore,
                     mechanics=mechanics)
        db.session.add(action)
        db.session.commit()
        return action

    def __repr__(self):
        return '{} belongs to character {}'.format(self.name, self.char_id)
