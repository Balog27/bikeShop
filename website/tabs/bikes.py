from flask import Blueprint, render_template, request
from website.models import Bikes
from flask_login import current_user, login_required

bikes_blueprint = Blueprint('bikes', __name__)

@bikes_blueprint.route('/bikes', methods=['GET'])
@login_required
def bikes():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '', type=str)
    filter_option = request.args.get('filter', '', type=str)
    bikes_per_page = 12

    query = Bikes.query

    if search_query:
        query = query.filter(Bikes.name.ilike(f'%{search_query}%'))

    if filter_option == 'price_asc':
        query = query.order_by(Bikes.price.asc())
    elif filter_option == 'price_desc':
        query = query.order_by(Bikes.price.desc())
    elif filter_option == 'alphabetical':
        query = query.order_by(Bikes.name.asc())

    all_bikes = query.paginate(page=page, per_page=bikes_per_page)

    return render_template("bikes.html", user=current_user, bikes=all_bikes)