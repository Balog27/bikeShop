from flask import Blueprint, render_template, request, flash, jsonify,redirect,url_for
from flask_login import login_required, current_user
from .models import Note,Review
from . import db
import json


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')#Gets the note from the HTML

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note
            db.session.add(new_note) #adding the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/add-review-form/<int:product_id>/<string:product_type>', methods=['GET'])
@login_required
def add_review_form(product_id, product_type):
    return render_template('add_review.html', product_id=product_id, product_type=product_type, user=current_user)

@views.route('/add-review', methods=['POST'])
@login_required
def add_review():
    review = request.form.get('review')
    rating = request.form.get('rating')
    product_id = request.form.get('product_id')
    product_type = request.form.get('product_type')
    if len(review) < 1:
        flash('Review is too short!', category='error')
    else:
        new_review = Review(description=review, rating=rating, product_id=product_id, product_type=product_type, user_id=current_user.id)
        db.session.add(new_review)
        db.session.commit()
        flash('Review added!', category='success')
    return redirect(url_for('views.view_reviews', product_id=product_id, product_type=product_type))


@views.route('/reviews/<int:product_id>/<string:product_type>', methods=['GET'])
@login_required
def view_reviews(product_id, product_type):
    reviews = Review.query.filter_by(product_id=product_id, product_type=product_type).all()
    return render_template('reviews.html', reviews=reviews, product_id=product_id, product_type=product_type, user=current_user)