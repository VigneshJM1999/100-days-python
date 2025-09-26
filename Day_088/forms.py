from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    location = StringField("Location", validators=[DataRequired()])
    seats = StringField("Seats", validators=[DataRequired()])
    has_sockets = BooleanField("Has Sockets?")
    has_toilet = BooleanField("Has Toilet?")
    has_wifi = BooleanField("Has Wifi?")
    can_take_calls = BooleanField("Can Take Calls?")
    coffee_price = StringField("Coffee Price", validators=[Optional()])
    submit = SubmitField("Add Cafe")