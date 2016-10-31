'''
[*] This file is for the entire shopping cart and its implementation

[!] This doesn't account for electronic recycling fees 
[!] This doesn't account for product weights
'''
from flask import Flask, flash, request
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required, NumberRange


# GLOBALS
SHIPPING_RATE = 5.50

#TODO: Display separate user not logged in form or redirect to login
class ShoppingCartFailForm(FlaskForm):
    pass


class CheckoutForm(FlaskForm):
    credit_card = IntegerField("Credit Card", 
            validators=[NumberRange(1000000000000000, 9999999999999999)])
    card_type = SelectField(validators=[Required()], choices=[(1, 'VISA'), (2, 'MASTERCARD')])
    checkout_btn = SubmitField('Checkout')


class ShoppingCartForm(FlaskForm):
    #item_count = IntegerField("Update Cart", validators=[NumberRange(0, 10)])
    update_btn = SubmitField('Update')


class ShoppingCart:
    def __init__(self, mysql, session):
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
        self.session = session
        self.cart = None

        self.get_cart_objects()

        self.form_fields = 0

        # Do this after the database has been queried for info
        #item_count = IntegerField("Update Cart", validators=[NumberRange(0, 10)])

        self.form = ShoppingCartForm()


    def calculateTotal(products, shipping_location):
        '''
        [*] Calculates the total at checkout

        [!] This is just a mockup implementation
        '''

        subtotal = 0.0
        total = 0.0
        taxRate = 0.0

        for product in products:
            subtotal += product.price

        total = subtotal + (subtotal * taxRate) + SHIPPING_RATE
        return total

    def get_cart_objects(self):
        grab_items_query = "SELECT * FROM cart WHERE username = '{}'"

        if 'username' in self.session:
            self.cursor.execute(grab_items_query.format(self.session.get('username')))
            self.cart = self.cursor.fetchall()

            print(self.cart, type(self.cart), self.cart[0][2])

            
        else: # TODO: Handle shopping cart w/o user acct. login
            flash('Please Login')
