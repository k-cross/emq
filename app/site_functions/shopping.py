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
from .order import Order, getDeliveryInfo


# GLOBALS
SHIPPING_RATE = 5.50
TAX_RATE = 0.095


class CheckoutForm(FlaskForm):
    credit_card = IntegerField("Credit Card",
                               validators=[NumberRange(1000000000000000, 9999999999999999)])
    card_type = SelectField(
        u'Type', coerce=int, choices=[(1, 'MASTERCARD'), (2, 'VISA')])
    checkout_btn = SubmitField('Checkout')


class ShoppingCartForm(FlaskForm):
    checkout_btn = SubmitField('Checkout')


class ShoppingCart:

    def __init__(self, mysql, session):
        self.queries = {
            'grab_items': "SELECT pname, cart.pid, price, quantity FROM cart, "
            + "inventory WHERE username='{}' and cart.pID=inventory.pID",
            'grab_orders': "SELECT * FROM orders WHERE transID = {}",
            'add_item': "INSERT INTO cart (username, pID) VALUES ('{}', '{}')",
            'update_cart': "UPDATE cart SET quantity={} "
            + "WHERE pID={} AND username='{}'",
            'checkout_query': "DELETE FROM cart WHERE username='{}'",
            'transaction_insert': "INSERT INTO transaction (userID, total_price, "
            + "status) VALUES ('{}', '{}', '{}')",
            'transaction_details_insert': "INSERT INTO transaction_details("
            + "transID,pID,price,quantity,storeID) VALUES ("
            + "'{}', '{}', '{}', '{}', '{}')",
            'order_update': "UPDATE orders SET storeAddress = %s, "
            +
            "deliveryEstimateSeconds = %s, deliverDistanceMeters = %s, "
            +
            "deliverDistanceMiles = %s, speed = %s WHERE transID = %s",
            'order_insert': "INSERT INTO orders(userID, transID, totalCost,"
            + "orderPlacedTime, items, deliveryAddress) SELECT user.userID "
                        + "AS userID, t.transID, t.total_price, t.trans_time, "
                        +
            "CONCAT('[', GROUP_CONCAT(td.pID SEPARATOR ', '), ']'), "
                        +
            "CONCAT(user.street, ', ', user.city, ', ', user.state, ' ',"
                        +
            "user.zip) FROM transaction t, transaction_details td, user "
                        + "WHERE t.transID = {} and t.transID = td.transID and t.userId = user.userID "
                        + "GROUP BY user.userID, t.transID;",
            'grab_address': "SELECT CONCAT(user.street, ', ', user.city, ', ', user.state, ' ', user.zip) FROM USER WHERE userID = {};",
            'update_status': "UPDATE transaction SET status = {} where transID = {}"
        }

        self.mysql = mysql
        self.session = session
        self.cart = None
        self.get_items()

        # Do this after the database has been queried for info
        self.form = ShoppingCartForm()


    def calculate_total(self):
        '''
        [*] Calculates the total at checkout

        [!] This is just a mockup implementation
        '''

        subtotal = 0.0
        total = 0.0

        for i in range(0, len(self.cart)):
            subtotal += float(self.cart[i][2]) * self.cart[i][3]

        tax = subtotal * TAX_RATE
        total = subtotal + tax + SHIPPING_RATE

        if subtotal > 0.0:
            return total, subtotal, tax, SHIPPING_RATE

        return 0.0, subtotal, 0.0, 0.0

    def get_items(self):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        if 'username' in self.session:
            cursor.execute(
                self.queries['grab_items'].format(self.session['username']))
            self.cart = cursor.fetchall()
        else:
            flash('Please Login')

        connection.close()

    def add_item(self, pid):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        cursor.execute(
            self.queries['add_item'].format(self.session['username'], pid))

        connection.commit()
        connection.close()

    def update_cart(self, pid, qty):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        cursor.execute(self.queries['update_cart'].format(
            qty,
            pid,
            self.session['username']
        ))
        connection.commit()
        connection.close()

        self.get_items()
        self.session['usercart'] = self.cart

    def checkout(self):
        connection = self.mysql.connect()
        cursor = connection.cursor()

        cursor.execute(self.queries['grab_address'].format(self.session['userid']))
        deliverAddress = cursor.fetchone()[0]
        
    
        (storeID, closest_store, deliverAddress, delivery_estimate_seconds, delivery_distance_meters,
         delivery_distance_miles, speed) = getDeliveryInfo(deliverAddress)
              
        cursor.execute(self.queries['transaction_insert'].format(
            self.session['userid'],
            self.session['total'],
            'Pending',
        ))
        transactionID = cursor.lastrowid

        # self.cart contains (product name, pID, price, quantity)
        for cartrow in self.cart:
            cursor.execute(self.queries['transaction_details_insert'].format(
                transactionID, cartrow[1], cartrow[2], cartrow[3], storeID))

        cursor.execute(self.queries['order_insert'].format(transactionID))
        connection.commit()
        cursor.execute(self.queries['grab_orders'].format(transactionID))


        cursor.execute(self.queries['order_update'],
                       (str(closest_store),
                        delivery_estimate_seconds,
                        delivery_distance_meters,
                        delivery_distance_miles,
                        speed,
                        transactionID
                        ))

        cursor.execute(
            self.queries['checkout_query'].format(self.session['username']))
        cursor.execute(self.queries['update_status'].format('\'Out for delivery\'' ,transactionID))
        connection.commit()
        connection.close()

        self.get_items()
        self.session['usercart'] = self.cart
