from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms.validators import Required

class CommentForm(Form):
  body = TextAreaField(validators=[Required()])
  author = TextField(validators=[Required()])
  submit = SubmitField('Post Comment')
  
  
class TipusForm(Form):
  name = TextField(validators=[Required()])
  email = TextField(validators=[Required()])
  subject = TextField(validators=[Required()])
  body = TextAreaField(validators=[Required()])  
  submit = SubmitField('Share')