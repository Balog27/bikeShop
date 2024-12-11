from flask import Blueprint, render_template, request,flash,redirect,url_for
from website.models import Bikes,Review
from website import db
from flask_login import current_user, login_required
from sqlalchemy import func

bikes_blueprint = Blueprint('bikes', __name__)

@bikes_blueprint.route('/bikes', methods=['GET'])
@login_required
def bikes():
    page = request.args.get('page', 1, type=int)
    bikes_per_page = 12
    all_bikes = Bikes.query.paginate(page=page, per_page=bikes_per_page)
    return render_template("bikes.html", user=current_user, bikes=all_bikes)

@bikes_blueprint.route('/bikes/filter_by_price_desc', methods=['GET'])
@login_required
def filter_by_price_desc():
    page = request.args.get('page', 1, type=int)
    bikes_per_page = 12
    all_bikes = Bikes.query.order_by(Bikes.price.desc()).paginate(page=page, per_page=bikes_per_page)
    return render_template("bikes.html", user=current_user, bikes=all_bikes)

@bikes_blueprint.route('/bikes/filter_by_price_asc', methods=['GET'])
@login_required
def filter_by_price_asc():
    page = request.args.get('page', 1, type=int)
    bikes_per_page = 12
    all_bikes = Bikes.query.order_by(Bikes.price.asc()).paginate(page=page, per_page=bikes_per_page)
    return render_template("bikes.html", user=current_user, bikes=all_bikes)

@bikes_blueprint.route('/bikes/filter_in_alphabetical_order', methods=['GET'])
@login_required
def filter_in_alphabetical_order():
    page = request.args.get('page', 1, type=int)
    bikes_per_page = 12
    all_bikes = Bikes.query.order_by(func.lower(Bikes.name).asc()).paginate(page=page, per_page=bikes_per_page)
    return render_template("bikes.html", user=current_user, bikes=all_bikes)

@bikes_blueprint.route('/bikes/search', methods=['GET'])
@login_required
def search():
    search = request.args.get('search', '').strip()
    page = request.args.get('page', 1, type=int)
    bikes_per_page = 12
    if search:
        all_bikes = Bikes.query.filter(func.lower(Bikes.name).contains(func.lower(search))).paginate(page=page, per_page=bikes_per_page)
    else:
        all_bikes = Bikes.query.paginate(page=page, per_page=bikes_per_page)
    return render_template("bikes.html", user=current_user, bikes=all_bikes)



