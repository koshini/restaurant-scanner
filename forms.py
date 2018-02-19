from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    location = StringField('location', validators=[DataRequired("Please enter a location")])
    submit = SubmitField('Search')

