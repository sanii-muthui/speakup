from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required 

class ReviewForm(FlaskForm):
   title = StringField('Comment')
   comment = TextAreaField('Enter your comment')
   submit = SubmitField('submit')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class PitchForm(FlaskForm):
    title = StringField('Post Title', validators=[Required()])
    pitch = TextAreaField('Post Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Innovation','Innovation'),('Technology','Technology'),('Photography','Photography'),('Poems','Poems'),('Film Production','Film Production')],validators=[Required()])
    submit = SubmitField(' SUBMIT POST')
class CommentForm(FlaskForm):
    description = TextAreaField('What do you think?',validators=[Required()])
    submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField('Submit:)')


class Downvote(FlaskForm):
	submit = SubmitField('Submit:)')
# class CommentForm(FlaskForm):
#     title = StringField('Comment')
#     comment = TextAreaField('Enter your comment')
#     submit = SubmitField('submit')