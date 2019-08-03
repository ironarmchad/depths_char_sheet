from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField


class CreateCharacterForm(FlaskForm):
    char_name = StringField('Name')
    char_lore = StringField('Lore')
    char_strength = IntegerField('Strength')
    char_reflex = IntegerField('Reflex')
    char_speed = IntegerField('Speed')
    char_awareness = IntegerField('Awareness')
    char_willpower = IntegerField('Willpower')
    char_imagination = IntegerField('Imagination')
    char_attunement = IntegerField('Attunement')
    char_faith = IntegerField('Faith')
    char_charisma = IntegerField('Charisma')
    char_luck = IntegerField('Luck')
    char_actions = StringField('Action Ids')
    submit = SubmitField()


class EditCharacterForm(FlaskForm):
    submit = SubmitField()
    # TODO: Edit character form


class DeleteCharacterForm(FlaskForm):
    submit = SubmitField()
    # TODO: Delete character form
