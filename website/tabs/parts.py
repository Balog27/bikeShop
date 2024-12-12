from sqlalchemy import func
from website.models import Parts
from website import db
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

parts_blueprint = Blueprint('parts', __name__)

@parts_blueprint.route('/parts', methods=['GET'])
@login_required
def parts():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '', type=str)
    filter_option = request.args.get('filter', '', type=str)

    query = Parts.query

    if search_query:
        query = query.filter(Parts.name.ilike(f'%{search_query}%'))

    if filter_option == 'price_asc':
        query = query.order_by(Parts.price.asc())
    elif filter_option == 'price_desc':
        query = query.order_by(Parts.price.desc())
    elif filter_option == 'alphabetical':
        query = query.order_by(Parts.name.asc())

    all_parts = query.paginate(page=page, per_page=parts_per_page)

    return render_template("parts.html", user=current_user, parts=all_parts)