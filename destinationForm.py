from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange


class DestinationForm(FlaskForm):
    journeyName = StringField("Name this Journey", validators=[DataRequired(), Length(min=2, max=20)])
    busNumber = IntegerField("Select Bus Number", validators=[DataRequired(), NumberRange(min=2, max=975,
                                                                                          message="Invalid Bus Number")])
    journeyFrom = StringField("From", validators=[DataRequired()])
    journeyTo = StringField("To", validators=[DataRequired()])
    alertMe = IntegerField("Alert Me Before {?} Stops", validators=[DataRequired()])
    submit = SubmitField("Submit")


class BusRoutes(FlaskForm):
    comment = StringField("Comment for the boys", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    comment = TextAreaField("Feedback:", validators=[DataRequired()])
    submit1 = SubmitField("Submit ")



