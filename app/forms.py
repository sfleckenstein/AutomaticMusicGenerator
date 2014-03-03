from flask.ext.wtf import Form
from wtforms import TextField, IntegerField
from wtforms.validators import ValidationError
from pyechonest import genre

class ChoiceForm(Form):
    # make these choices from the Echo Nest API
    genre = TextField('genre')
    tempo = TextField('tempo')
    time_signature = TextField('time_signature')
    key_signature = IntegerField('key_signature')
    
    def validate_genre(form, field):
        if genre not in genre.list()
            raise ValidationError("Genre must be one from the Echo nest list.")

    def validate_key_signature(form, field):
        if field.data < 0 or field.data > 11:
            raise ValidationError("Key signature must be a value from 0 to 11")
