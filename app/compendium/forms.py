from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class EditCompendForm(FlaskForm):
    page_name = StringField("Page Name", validators=[DataRequired()])
    contents = StringField("Contents", widget=TextArea(), render_kw={"rows": 20, "cols": 20})
    submit = SubmitField('Update')


class CreateCompendForm(FlaskForm):
    page_name = StringField("Page Name", validators=[DataRequired()])
    contents = StringField("Contents", widget=TextArea(), render_kw={'rows':20, 'cols': 20})
    submit = SubmitField('Create')