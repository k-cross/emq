'''
[*] This file is for setting up the account creation logic
'''
from flask import Flask, flash, request
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField
from wtforms.validators import Required, NumberRange, Email
from .order import Order, getDeliveryInfo, isDeliverable


class AccountForm(FlaskForm):
    username = StringField("Username", validators=[Required])
    password = PasswordField(validators=[Required])
    email = StringField(validators=[Required, Email])
    firstname = StringField("First Name", validators=[Required])
    lastname = StringField("Last Name", validators=[Required])
    address = StringField("Street Address", validators=[Required])
    city = StringField("City", validators=[Required])
    zipcode = IntegerField(validators=[NumberRange(10000, 99999)])
    state = SelectField('State', choices=[('AL','Alabama'),
                                          ('AK','Alaska'),
                                          ('AZ','Arizona'),
                                          ('AR','Arkansas'),
                                          ('CA','California'),
                                          ('CO','Colorado'),
                                          ('CT','Connecticut'),
                                          ('DE','Delaware'),
                                          ('DC','District of Columbia'),
                                          ('FL','Florida'),
                                          ('GA','Georgia'),
                                          ('HI','Hawaii'),
                                          ('ID','Idaho'),
                                          ('IL','Illinois'),
                                          ('IN','Indiana'),
                                          ('IA','Iowa'),
                                          ('KS','Kansas'),
                                          ('KY','Kentucky'),
                                          ('LA','Louisiana'),
                                          ('ME','Maine'),
                                          ('MD','Maryland'),
                                          ('MA','Massachusetts'),
                                          ('MI','Michigan'),
                                          ('MN','Minnesota'),
                                          ('MS','Mississippi'),
                                          ('MO','Missouri'),
                                          ('MT','Montana'),
                                          ('NE','Nebraska'),
                                          ('NV','Nevada'),
                                          ('NH','New Hampshire'),
                                          ('NJ','New Jersey'),
                                          ('NM','New Mexico'),
                                          ('NY','New York'),
                                          ('NC','North Carolina'),
                                          ('ND','North Dakota'),
                                          ('OH','Ohio'),
                                          ('OK','Oklahoma'),
                                          ('OR','Oregon'),
                                          ('PA','Pennsylvania'),
                                          ('RI','Rhode Island'),
                                          ('SC','South Carolina'),
                                          ('SD','South Dakota'),
                                          ('TN','Tennessee'),
                                          ('TX','Texas'),
                                          ('UT','Utah'),
                                          ('VT','Vermont'),
                                          ('VA','Virginia'),
                                          ('WA','Washington'),
                                          ('WV','West Virginia'),
                                          ('WI','Wisconsin'),
                                          ('WY','Wyoming')], validators=[Required])
    submit_btn = SubmitField('Create Account', )
            #validators=[addressValidator(address, city, zipcode, state)])

    def addressValidator(form, address, city, zipcode, state):
        # TODO: finish
        #if (shit happens):
        #    raise ValidationError("Address Does Not Exist")
        pass
