from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, NumberRange

from shopping_cart import ShoppingCart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test' # This really should go in a seperate file
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        print(e)

@app.route('/createAccount')
def createAccount():
    try:
        return render_template('createAccount.html')
    except Exception as e:
        print(e)

@app.route('/login')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        print(e)

@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    items = None
    form = ShoppingCart()

    if form.validate_on_submit():
        items = form.item_count.data
    return render_template('shopping_cart.html', form=form, items=items)

@app.route('/trackDelivery')
def trackDelivery():
    key = 'AIzaSyB7BkwSe4-5V14C3wY301HVolGN2IdO2PA'
    startLocation = '777 Story Rd, San Jose, CA 95122' # walmart
    endLocation = '1 Washington Sq, San Jose, CA 95192'  # SJSU
    try:
        return render_template('map.html', key=key, startLocation=startLocation, endLocation=endLocation)
    except Exception as e:
        print(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
 
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
