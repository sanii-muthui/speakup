from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm
from ..models import Review,User,Pitch,Upvote,Downvote
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    #category = Category.get_categories()
 
    title = 'Home'
    return render_template('index.html', title = title)


@main.route('/pitches',methods = ['GET','POST'])
@login_required
def new_pitch():
    name = "Pitch"
    title = 'Welcome,Pitch your one-minute pitch!'
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.validate_on_submit():
        
        title=form.title.data
        post=form.pitch.data
        category = form.category.data
        new_pitch = Pitch(title = title,post=post,category=category)
        
        db.session.add(new_pitch)
        db.session.commit()

         
        return redirect(url_for('main.post_pitch'))


    return render_template('post.html',title = title, name=name, pitch_form =form)


@main.route('/posts')
@login_required
def post_pitch():

    pitches = Pitch.query.all()
    return render_template('new_pitch.html',pitches = pitches)


@main.route('/reviews/<id>',methods = ['GET', 'POST'])
def post_review(id):
    pitch = Pitch.query.filter_by(id=id).first()
    
    form = ReviewForm()
    
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        
        new_review = Review(review_title = title, review = review, pitch_id=id, posted_by=current_user.username)
        new_review.save_review()
        return redirect(url_for('.post_review',id=pitch.id))
    return render_template('reviews.html',form=form, pitch=pitch)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        print(path)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))





@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))