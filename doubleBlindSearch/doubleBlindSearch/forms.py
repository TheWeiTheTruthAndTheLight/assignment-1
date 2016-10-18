from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, TextField
from wtforms.validators import DataRequired


class InitialSearchForm(FlaskForm):
    query = TextField('Query', validators=[DataRequired()])

    valueA      = HiddenField(validators=[DataRequired()])
    valueB      = HiddenField(validators=[DataRequired()])
    valueC      = HiddenField(validators=[DataRequired()])
    nameA       = HiddenField(validators=[DataRequired()])
    nameB       = HiddenField(validators=[DataRequired()])
    nameC       = HiddenField(validators=[DataRequired()])
    meanBing    = HiddenField(validators=[DataRequired()])
    meanGoogle  = HiddenField(validators=[DataRequired()])
    meanYahoo   = HiddenField(validators=[DataRequired()])
    trialNumber = HiddenField(validators=[DataRequired()])


class TrialForm(FlaskForm):
    query  = TextField('Next query', validators=[DataRequired()])

    valueA = IntegerField('Engine A', validators=[DataRequired()])
    valueB = IntegerField('Engine B', validators=[DataRequired()])
    valueC = IntegerField('Engine C', validators=[DataRequired()])

    nameA       = HiddenField(validators=[DataRequired()])
    nameB       = HiddenField(validators=[DataRequired()])
    nameC       = HiddenField(validators=[DataRequired()])
    meanBing    = HiddenField(validators=[DataRequired()])
    meanGoogle  = HiddenField(validators=[DataRequired()])
    meanYahoo   = HiddenField(validators=[DataRequired()])
    trialNumber = HiddenField(validators=[DataRequired()])
