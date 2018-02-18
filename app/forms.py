from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired

class contactForm(Form):
    name=StringField('Name',validators=[DataRequired()]);
    email=StringField('Email',validators=[DataRequired()]);
    subject=StringField('Subject',validators=[DataRequired()]);
    message=TextAreaField('Message',validators=[DataRequired()]);
