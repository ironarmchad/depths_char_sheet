from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, ValidationError
from wtforms.validators import DataRequired


def check_empty(form, field):
    if field.data == '':
        raise ValidationError('Field must be filled')


class CreateCharacterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    char_type = SelectField('Type', choices=[('', '---'), ('player', 'Player'), ('npc', 'NPC')], validators=[check_empty])
    game_id = SelectField('Type', coerce=int)
    lore = TextAreaField('Lore', render_kw={'rows': 10, 'cols': 20})
    strength = IntegerField('Strength', validators=[DataRequired()])
    reflex = IntegerField('Reflex', validators=[DataRequired()])
    vitality = IntegerField('Vitality', validators=[DataRequired()])
    speed = IntegerField('Speed', validators=[DataRequired()])
    awareness = IntegerField('Awareness', validators=[DataRequired()])
    willpower = IntegerField('Willpower', validators=[DataRequired()])
    imagination = IntegerField('Imagination', validators=[DataRequired()])
    attunement = IntegerField('Attunement', validators=[DataRequired()])
    faith = IntegerField('Faith', validators=[DataRequired()])
    charisma = IntegerField('Charisma', validators=[DataRequired()])
    luck = IntegerField('Luck', validators=[DataRequired()])


class ActionCreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    act_type = SelectField('Type', choices=[('', '---'), ('natural', 'NATURAL'), ('super', 'SUPERNATURAL'), ('item', 'ITEM')], validators=[check_empty])
    lore = TextAreaField('Lore', render_kw={'rows': 10, 'cols': 20})
    mechanics = TextAreaField('Mechanics', render_kw={'rows': 10, 'cols': 20})

