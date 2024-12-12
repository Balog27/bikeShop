from flask import Blueprint, render_template, request
from sqlalchemy import func
from website.models import Accessories
from flask_login import current_user, login_required

accessories_blueprint = Blueprint('accessories', __name__)

@accessories_blueprint.route('/accessories', methods=['GET'])
@login_required
def accessories():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '', type=str)
    filter_option = request.args.get('filter', '', type=str)
    accessories_per_page = 12

    query = Accessories.query

    if search_query:
        query = query.filter(Accessories.name.ilike(f'%{search_query}%'))

    if filter_option == 'price_asc':
        query = query.order_by(Accessories.price.asc())
    elif filter_option == 'price_desc':
        query = query.order_by(Accessories.price.desc())
    elif filter_option == 'alphabetical':
        query = query.order_by(Accessories.name.asc())

    all_accessories = query.paginate(page=page, per_page=accessories_per_page)

    return render_template("accessories.html", user=current_user, accessories=all_accessories)