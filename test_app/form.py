
from wtforms import Form, FloatField, IntegerField, validators

class InputForm(Form):
    x = IntegerField(label="x values", default=10, validators=[validators.InputRequired()])
    y = IntegerField(label="y values", default=10, validators=[validators.InputRequired()])
