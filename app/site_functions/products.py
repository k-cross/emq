from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask import Blueprint, render_template, abort, session, flash, redirect, url_for


class Products(FlaskForm):
    product_list = []

    # TODO: grab and display all products from the db with add to cart buttons

    def add_to_cart():
        # TODO: Implement the feature
        pass

@store_blueprint.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id=0): 
    cart = Add_to_cart(prefix="cart")

    product = Product.query.get(id)

    if cart.validate_on_submit():
        if 'cart' in session:
            if not any(product.name in d for d in session['cart']):
                session['cart'].append({product.name: cart.quantity.data})
            elif any(product.name in d for d in session['cart']):
                for d in session['cart']:
                    d.update((k, cart.quantity.data) for k, v in d.items() if k == product.name)

        else:
            session['cart' .format(id)] = [{product.name: cart.quantity.data}]


        return redirect(url_for('products.html'))
