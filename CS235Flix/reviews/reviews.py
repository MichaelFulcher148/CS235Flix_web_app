from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, IntegerField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.widgets.html5 import RangeInput, NumberInput
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange
import CS235Flix.reviews.services as services
from CS235Flix.authentication.authentication import login_required
import CS235Flix.memory_repository.abtractrepository as repo

reviews_blueprint = Blueprint('review_bp', __name__)

class ReviewForm(FlaskForm):
    content = TextAreaField('Comment', [DataRequired(message='Comment Text is required'), Length(min=10, message='Comment must be at lease 10 characters')])
    # rating = IntegerField('Rating', [DataRequired(message='Rating is required'), NumberRange(min=1, max=10)], widget=NumberInput(min=1, max=10))
    rating = IntegerRangeField(label='Rating', validators=[DataRequired(message='Rating is required'), NumberRange(min=1, max=10)], widget=RangeInput(step=1))
    submit = SubmitField('Submit Review')

@reviews_blueprint.route('/add_review', methods=['GET', 'POST'])
@login_required
def add_review():
    form = ReviewForm()
    movie_name = request.args.get('title')
    release_date = request.args.get('date')
    print('hello')
    if form.validate_on_submit():
        #  check if movie title exists.
        print('validated')
        services.add_review(movie_name, int(release_date), form.content.data, form.rating.data, repo.repository_instance)
        return redirect(f"{url_for('browse_bp.view_movie_info')}?movie_name={movie_name}&date={release_date}")
    else:
        print('not valid')
    return render_template('write_review.html', form=form, title=movie_name, release_year=release_date)
