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
TAX_RATE = 0.095

#TODO: Display separate user not logged in form or redirect to login
class ShoppingCartFailForm(FlaskForm):
    pass


class CheckoutForm(FlaskForm):
    credit_card = IntegerField("Credit Card", 
            validators=[NumberRange(1000000000000000, 9999999999999999)])
    card_type = SelectField(u'Type', choices=[(1, 'VISA'), (2, 'MASTERCARD')])
    checkout_btn = SubmitField('Checkout')


class ShoppingCartForm(FlaskForm):
    # TODO: Add checkout button
    update_btn = SubmitField('Update')
    checkout_btn = SubmitField('Checkout')


class ShoppingCartButtonForm(FlaskForm):
    update_btn = SelectField(u'Quantity', choices=[(i,i) for i in range(1, 11)])


class ShoppingCart:
    def __init__(self, mysql, session):
        self.queries = {
                'grab_items' : "SELECT pname, cart.pid, price, quantity FROM cart, "
                    + "inventory WHERE username='{}' and cart.pID=inventory.pID",
                'transaction_query' : "INSERT INTO transaction (userID, total_price, "
                    + "status) VALUES ('{}', '{}', '{}')"
                }

        self.mysql = mysql
        self.session = session
        self.cart = None
        self.get_items()

        # Do this after the database has been queried for info
        self.form = ShoppingCartForm()
        self.item_forms = [ShoppingCartButtonForm() for i in range(0, len(self.cart))]

        for i in range(0, len(self.item_forms)):
            self.item_forms[i].update_btn.id='qty_{}'.format(i)


    def calculate_total(self):
        '''
        [*] Calculates the total at checkout

        [!] This is just a mockup implementation
        '''

        subtotal = 0.0
        total = 0.0

        for i in range(0, len(self.cart)):
            subtotal += float(self.cart[i][2]) * self.cart[i][3]

        total = subtotal + (subtotal * TAX_RATE) + SHIPPING_RATE
        return total, subtotal, TAX_RATE, SHIPPING_RATE


    def get_items(self):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        if 'username' in self.session:
            cursor.execute(self.queries['grab_items'].format(self.session['username']))
            self.cart = cursor.fetchall()
        else: # TODO: Handle shopping cart w/o user acct. login
            flash('Please Login')

        connection.close()


    #TODO: Implement
    def add_item(self, pid):
        pass


    #TODO: Implement
    def update_cart(self):
        pass
