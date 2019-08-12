from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class GameCreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lore = TextAreaField('Lore', render_kw={'rows': 10, 'cols': 20})
