from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#todo needs to be added to the __init__ and also it needs a template

# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.Sting(5))
#     description = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class Bikes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(150))
    image = db.Column(db.String(150))
    def __repr__(self):
        return f"Bike('{self.name}', '{self.price}', '{self.description}', '{self.image}')"

    def average_rating(self):
        reviews = Review.query.filter_by(product_id=self.id, product_type='bike').all()
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)

    def number_of_ratings(self):
        return Review.query.filter_by(product_id=self.id, product_type='bike').count()

class Parts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(150))
    image = db.Column(db.String(150))
    def __repr__(self):
        return f"Part('{self.name}', '{self.price}', '{self.description}', '{self.image}')"

    def average_rating(self):
        reviews = Review.query.filter_by(product_id=self.id, product_type='part').all()
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)

    def number_of_ratings(self):
        return Review.query.filter_by(product_id=self.id, product_type='part').count()


class Accessories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(150))
    image = db.Column(db.String(150))
    def __repr__(self):
        return f"Accessory('{self.name}', '{self.price}', '{self.description}', '{self.image}')"

    def average_rating(self):
        reviews = Review.query.filter_by(product_id=self.id, product_type='accessory').all()
        if not reviews:
            return 0
        return sum(review.rating for review in reviews) / len(reviews)

    def number_of_ratings(self):
        return Review.query.filter_by(product_id=self.id, product_type='accessory').count()


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.relationship('CartItem', backref='cart', lazy=True)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer)
    product_type = db.Column(db.String(50))  # 'bike', 'part', 'accessory'
    quantity = db.Column(db.Integer, default=1)

    def get_product(self):
        if self.product_type == 'bike':
            return Bikes.query.get(self.product_id)
        elif self.product_type == 'part':
            return Parts.query.get(self.product_id)
        elif self.product_type == 'accessory':
            return Accessories.query.get(self.product_id)
        return None


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float)
    description = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer)
    product_type = db.Column(db.String(50))  # 'bike', 'part', 'accessory'

    def __repr__(self):
        return f"Review('{self.rating}', '{self.description}', '{self.date}')"