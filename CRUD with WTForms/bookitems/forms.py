from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,HiddenField
from wtforms.validators import DataRequired, Length


class BookForm(FlaskForm):
    id = HiddenField()
    name = StringField('Book-name', validators=[DataRequired(), Length(min=2, max=120)])
    author = StringField('Author', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('ADD')
    update = SubmitField('Update')


class UpdateForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    new_name = StringField('Book-name', validators=[DataRequired(), Length(min=2, max=120)])
    new_author = StringField('Author', validators=[DataRequired()])
    new_price = StringField('Price', validators=[DataRequired()])
    update = SubmitField('Update')