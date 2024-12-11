from sqlalchemy import func
from website.models import Parts
from website import db
from flask import Blueprint, render_template, request
from flask_login import current_user,login_required
parts_blueprint = Blueprint('parts', __name__)

@parts_blueprint.route('/parts', methods=['GET'])
@login_required
def parts():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    all_parts = Parts.query.paginate(page=page, per_page=parts_per_page)
    return render_template("parts.html", user =current_user, parts=all_parts)


@parts_blueprint.route('/parts/filter_by_price_desc', methods=['GET'])
@login_required
def filter_by_price_desc():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    all_parts = Parts.query.order_by(Parts.price.desc()).paginate(page = page, per_page=parts_per_page)
    return render_template("parts.html", user=current_user, parts=all_parts)

@parts_blueprint.route('/parts/filter_by_price_asc', methods=['GET'])
@login_required
def filter_by_price_asc():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    all_parts = Parts.query.order_by(Parts.price.asc()).paginate(page=page, per_page=parts_per_page)
    return render_template("parts.html", user=current_user, parts=all_parts)

@parts_blueprint.route('/parts/filter_in_alphabetical_order', methods=['GET'])
@login_required
def filter_in_alphabetical_order():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    all_parts = Parts.query.order_by(func.lower(Parts.name).asc()).paginate(page=page, per_page=parts_per_page)
    return render_template("parts.html", user=current_user, parts=all_parts)


@parts_blueprint.route('/parts/search', methods=['GET'])
@login_required
def search():
    parts_per_page = 12
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '').strip()
    if search:
        all_parts = Parts.query.filter(func.lower(Parts.name).contains(func.lower(search))).paginate(page=page, per_page=parts_per_page)
    else:
        all_parts = Parts.query.paginate(page=page, per_page=parts_per_page)
    render_template("parts.html", user=current_user, parts=all_parts)