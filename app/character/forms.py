from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class CreateCharacterForm(FlaskForm):
    char_name = StringField('Name', validators=[DataRequired()])
    char_lore = StringField('Lore')
    char_strength = IntegerField('Strength', validators=[DataRequired()])
    char_reflex = IntegerField('Reflex', validators=[DataRequired()])
    char_vitality = IntegerField('Vitality', validators=[DataRequired()])
    char_speed = IntegerField('Speed', validators=[DataRequired()])
    char_awareness = IntegerField('Awareness', validators=[DataRequired()])
    char_willpower = IntegerField('Willpower', validators=[DataRequired()])
    char_imagination = IntegerField('Imagination', validators=[DataRequired()])
    char_attunement = IntegerField('Attunement', validators=[DataRequired()])
    char_faith = IntegerField('Faith', validators=[DataRequired()])
    char_charisma = IntegerField('Charisma', validators=[DataRequired()])
    char_luck = IntegerField('Luck', validators=[DataRequired()])
    submit = SubmitField()


class EditCharacterForm(FlaskForm):
    char_name = StringField('Name', validators=[DataRequired()])
    char_lore = StringField('Lore')
    char_strength = IntegerField('Strength', validators=[DataRequired()])
    char_reflex = IntegerField('Reflex', validators=[DataRequired()])
    char_vitality = IntegerField('Vitality', validators=[DataRequired()])
    char_speed = IntegerField('Speed', validators=[DataRequired()])
    char_awareness = IntegerField('Awareness', validators=[DataRequired()])
    char_willpower = IntegerField('Willpower', validators=[DataRequired()])
    char_imagination = IntegerField('Imagination', validators=[DataRequired()])
    char_attunement = IntegerField('Attunement', validators=[DataRequired()])
    char_faith = IntegerField('Faith', validators=[DataRequired()])
    char_charisma = IntegerField('Charisma', validators=[DataRequired()])
    char_luck = IntegerField('Luck', validators=[DataRequired()])
    submit = SubmitField()


class DeleteCharacterForm(FlaskForm):
    submit = SubmitField()
    # TODO: Delete character form
