from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired


class InitialSearchForm(FlaskForm):
    query = TextField('query', validators=[DataRequired()])
