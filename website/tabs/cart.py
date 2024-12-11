from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from website.models import Cart, CartItem, Bikes, Parts, Accessories
from website import db

cart_blueprint = Blueprint('cart', __name__)

@cart_blueprint.route('/cart', methods=['GET'])
@login_required
def view_cart():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    total_price = 0
    if cart and cart.items:
        for item in cart.items:
            product = item.get_product()
            total_price += product.price * item.quantity
    return render_template('cart.html', cart=cart, total_price=total_price, user = current_user)


@cart_blueprint.route('/cart/add', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id')
    product_type = request.form.get('product_type')
    quantity = int(request.form.get('quantity', 1))
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id, product_type=product_type).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, product_type=product_type, quantity=quantity)
        db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('cart.view_cart'))

@cart_blueprint.route('/cart/remove', methods=['POST'])
@login_required
def remove_from_cart():
    item_id = request.form.get('item_id')
    cart_item = CartItem.query.get(item_id)
    if cart_item and cart_item.cart.user_id == current_user.id:

        db.session.delete(cart_item)
        db.session.commit()
    return redirect(url_for('cart.view_cart'))


# @cart_blueprint.route('/cart/checkout', methods=['POST'])
# @login_required
# def checkout():
#     cart = Cart.query.filter_by(user_id=current_user.id).first()
#     if cart and cart.items:
#         # Process the checkout (e.g., clear the cart, create an order, etc.)
#         cart.items = []
#         db.session.commit()
#         return redirect(url_for('cart.view_cart'))
#     return redirect(url_for('cart.view_cart'))

@cart_blueprint.route('/cart/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    return render_template('checkout.html')


@cart_blueprint.route('cart/process_checkout',methods= ['POST'])
@login_required
def process_checkout():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    payment_method = request.form.get('payment_method')

    if not name or not address or not phone or not payment_method:
        return redirect(url_for('cart.view_cart'))

    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if cart and cart.items:
        # Process the checkout (e.g., clear the cart, create an order, etc.)
        cart.items = []
        db.session.commit()
        return redirect(url_for('cart.view_cart'))

    return redirect(url_for('cart.view_cart'))