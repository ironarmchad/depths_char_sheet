from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length


def check_empty(form, field):
    if field.data == '':
        raise ValidationError('Field must be filled')


def stat_range(form, field):
    if field.data > 21:
        raise ValidationError('Value must be less than 21.')
    elif field.data < 1:
        raise ValidationError('Value must be greater than 0')


class CharacterCreateCoreForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    char_type = SelectField('Type', choices=[('', '---'), ('player', 'Player'), ('npc', 'NPC')], validators=[check_empty])
    game_id = SelectField('Type', coerce=int)
    lore = TextAreaField('Lore', render_kw={'rows': 10, 'cols': 20})
    summary = TextAreaField('Summary', render_kw={'rows': 3, 'cols': 20})


class CharacterCreateStatsForm(FlaskForm):
    strength = IntegerField('Strength', validators=[DataRequired(), stat_range])
    reflex = IntegerField('Reflex', validators=[DataRequired(), stat_range])
    vitality = IntegerField('Vitality', validators=[DataRequired(), stat_range])
    speed = IntegerField('Speed', validators=[DataRequired(), stat_range])
    awareness = IntegerField('Awareness', validators=[DataRequired(), stat_range])
    willpower = IntegerField('Willpower', validators=[DataRequired(), stat_range])
    imagination = IntegerField('Imagination', validators=[DataRequired(), stat_range])
    attunement = IntegerField('Attunement', validators=[DataRequired(), stat_range])
    faith = IntegerField('Faith', validators=[DataRequired(), stat_range])
    charisma = IntegerField('Charisma', validators=[DataRequired(), stat_range])
    luck = IntegerField('Luck', validators=[DataRequired(), stat_range])


class ActionCreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    act_type = SelectField('Type', choices=[('', '---'), ('natural', 'NATURAL'), ('super', 'SUPERNATURAL'), ('item', 'ITEM')], validators=[check_empty])
    lore = TextAreaField('Lore', render_kw={'rows': 10, 'cols': 20})
    summary = TextAreaField('Summary', render_kw={'rows': 3, 'cols': 20}, validators=[Length(max=150)])
    mechanics = TextAreaField('Mechanics', render_kw={'rows': 3, 'cols': 20}, validators=[Length(max=150)])

