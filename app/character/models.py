from app import db


class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    lore = db.Column(db.String)
    strength = db.Column(db.Integer, nullable=False)
    reflex = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
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
                         char_speed,
                         char_awareness,
                         char_willpower,
                         char_imagination,
                         char_attunement,
                         char_faith,
                         char_luck,
                         char_charisma,
                         char_actions):
        character = cls(owner=char_owner,
                        name=char_name,
                        lore=char_lore,
                        strength=char_strength,
                        reflex=char_reflex,
                        speed=char_speed,
                        awareness=char_awareness,
                        willpower=char_willpower,
                        imagination=char_imagination,
                        attunement=char_attunement,
                        faith=char_faith,
                        luck=char_luck,
                        charisma=char_charisma,
                        actions=char_actions)
        db.session.add(character)
        db.session.commit()
        return character


class Action():
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    lore = db.Column(db.String)
    script = db.Column(db.String, nullable=False)
    # TODO: Write the Action db...
