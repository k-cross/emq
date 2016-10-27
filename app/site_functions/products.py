from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField

class Products(FlaskForm):
    product_list = []

    # TODO: grab and display all products from the db with add to cart buttons

    def add_to_cart():
        # TODO: Implement the feature
        pass
