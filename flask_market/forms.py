import uuid
from flask_wtf import FlaskForm
from wtforms import validators, StringField, \
    SubmitField, FloatField, FileField
from wtforms.validators import InputRequired


class AddProductForm(FlaskForm):
    id = str(uuid.uuid4())
    name = StringField('Name', [validators.Length(min=1, max=20)])
    description = StringField('Description',
                              [validators.Length(min=1, max=2000)])
    price = FloatField('Price', [validators.number_range(0, 1000)])
    image = FileField('Image', validators=[InputRequired()])
    submit = SubmitField('Save')


class FilterForm(FlaskForm):
    price = FloatField('Price', [validators.number_range(0, 100000)])
    submit = SubmitField('Search')


class AddMarketForm(FlaskForm):
    id = str(uuid.uuid4())
    name = StringField('Name', [validators.Length(min=1, max=20)])
    location = StringField('Location', [validators.Length(min=1, max=25)])
    image = FileField('Image', validators=[InputRequired()])
    submit = SubmitField('Save')


class FilterMarketForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=3, max=20)])
    submit = SubmitField('Search')
