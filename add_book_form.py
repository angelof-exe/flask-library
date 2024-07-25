from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, URL, InputRequired, NumberRange, ValidationError, Length
import datetime

def validate_year(form, field):
    current_year = datetime.datetime.now().year
    if field.data < 1900 or field.data > current_year:
        raise ValidationError('Year must be between 1900 and the current year.')

class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    # book_year = StringField('Book Year', validators=[DataRequired()])
    book_year = IntegerField('Book Year', [InputRequired(),NumberRange(min=1900, max=datetime.datetime.now().year),validate_year])
    author_name = StringField('Author Name', validators=[DataRequired()])
    wikipedia_link = StringField('Wikipedia Link', validators=[DataRequired(), URL()])
    book_description = StringField('Book Description', validators=[DataRequired(), Length(max=200)])
    image_url = StringField('Image URL', validators=[DataRequired(), URL()])

    submit = SubmitField('Submit')