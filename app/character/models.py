from app import db


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False, index=True)
    char_type = db.Column(db.String(10), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
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
                         owner,
                         name,
                         char_type,
                         game_id,
                         lore):
        character = cls(owner=owner,
                        name=name,
                        char_type=char_type,
                        game_id=game_id,
                        lore=lore,
                        strength=1,
                        reflex=1,
                        vitality=1,
                        speed=1,
                        awareness=1,
                        willpower=1,
                        imagination=1,
                        attunement=1,
                        faith=1,
                        luck=1,
                        charisma=1)
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
