from flask import Blueprint, render_template, request
from sqlalchemy import func
from website.models import Accessories
from website import db

from flask_login import current_user, login_required

accessories_blueprint = Blueprint('accessories', __name__)

@accessories_blueprint.route('/accessories', methods=['GET'])
@login_required
def accessories():

    page = request.args.get('page', 1, type=int)
    accessories_per_page = 12
    all_accessories = Accessories.query.paginate(page=page, per_page=accessories_per_page)
    return render_template("accessories.html", user=current_user, accessories=all_accessories)


@accessories_blueprint.route('/accessories/filter_by_price_desc', methods=['GET'])
@login_required
def filter_by_price_desc():
    page = request.args.get('page', 1, type=int)
    accessories_per_page = 12

    all_accessories = Accessories.query.order_by(Accessories.price.desc()).paginate(page=page, per_page=accessories_per_page)
    return render_template("accessories.html", user=current_user, accessories=all_accessories)

@accessories_blueprint.route('/accessories/filter_by_price_asc', methods=['GET'])
@login_required
def filter_by_price_asc():
    page = request.args.get('page', 1, type=int)
    accessories_per_page = 12
    all_accessories = Accessories.query.order_by(Accessories.price.asc()).paginate(page=page, per_page=accessories_per_page)
    return render_template("accessories.html", user=current_user, accessories=all_accessories)


@accessories_blueprint.route('/accesories/search', methods=['GET'])
@login_required
def search():
    page = request.args.get('page', 1, type=int)
    accessories_per_page = 12
    search = request.args.get('search', '').strip()
    if search:
        all_accessories = Accessories.query.filter(func.lower(Accessories.name).contains(func.lower(search))).paginate(page=page, per_page=accessories_per_page)
    else:
        all_accessories = Accessories.query.paginate(page=page, per_page=accessories_per_page)
    render_template("accessories.html", user=current_user, accessories=all_accessories)