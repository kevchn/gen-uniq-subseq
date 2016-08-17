from wtforms import Form, IntegerField, validators

class InputForm(Form):
    index_5p = IntegerField(
        label='1-based index where motif starts from 5p side (nt)', default=3,
        validators=[validators.InputRequired()])
    motif_size = IntegerField(
        label='size of motif (nt)', default=10,
        validators=[validators.InputRequired()])
