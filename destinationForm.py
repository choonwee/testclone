from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class DestinationForm(FlaskForm):
    journeyName = StringField("Name this Journey", validators=[DataRequired(), Length(min=2, max=20)])
    busNumber = IntegerField("Select Bus Number", validators=[DataRequired()])
    journeyFrom = StringField("From", validators=[DataRequired()])
    journeyTo = StringField("To", validators=[DataRequired()])
    alertMe = IntegerField("Alert Me Before {?} Stops", validators=[DataRequired()])
    submit = SubmitField("Submit")