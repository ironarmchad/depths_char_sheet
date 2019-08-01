from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class EditCompendForm(FlaskForm):
    page_name = StringField("Page Name", validators=[DataRequired()])
    page_content = StringField("Contents", render_kw={"rows": 70, "cols": 20})
    submit = SubmitField('Update')


class CreateCompendForm(FlaskForm):
    page_name = StringField("Page Name", validators=[DataRequired()])
    page_content = StringField("Contents", widget=TextArea())
    submit = SubmitField('Create')