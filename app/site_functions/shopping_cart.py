'''
[*] This file is for the entire shopping cart and its implementation

[!] This doesn't account for electronic recycling fees 
[!] This doesn't account for product weights
'''
from flask import Flask
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, NumberRange


# GLOBALS
SHIPPING_RATE = 5.50

class ShoppingCartForm(FlaskForm):
    item_count = IntegerField("Update Cart", validators=[NumberRange(0, 10)])
    submit = SubmitField('Submit')

class ShoppingCart:
    def __init__(self, mysql):
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
        self.form = ShoppingCartForm()

    def calculateTotal(products, shipping_location):
        '''
        [*] Calculates the total at checkout

        [!] This is just a mockup implementation
        '''

        # TODO: Add database driver calls to get needed info
        subtotal = 0.0
        total = 0.0
        taxRate = 0.0

        for product in products:
            subtotal += product.price

        total = subtotal + (subtotal * taxRate) + SHIPPING_RATE
        return total


