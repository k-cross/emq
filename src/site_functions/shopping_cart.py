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

class ShoppingCart(FlaskForm):
    item_count = IntegerField("Update Cart", validators=[NumberRange(0, 10)])
    submit = SubmitField('Submit')

    def __init__(self, mysql):
        # TODO: make item_count update based on items in sc db
        #self.db_connection = mysql.connect()
        self.cursor = mysql.get_db().cursor()
        #self.item_count = IntegerField("Update Cart", validators=[NumberRange(0, 10)])
        #self.submit = SubmitField('Submit')
        #item_count = []
        
        #item_count.append(
        #    for items in db:
        #        IntegerField("Update Cart", validators=[NumberRange(0, 10)]))

        #self.db_connection.close()

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
