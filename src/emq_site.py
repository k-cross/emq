from flask import Flask, render_template, request, redirect, jsonify, flash, url_for
from flask import flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, NumberRange
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
# Our written additions
from settings import app_setup
from site_functions.shopping_cart import ShoppingCart
from site_functions import order

# Initialize Application
app = app_setup()
mysql = MySQL()
mysql.init_app(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

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

@app.route('/addUser',methods = ['POST', 'GET'])
def addUser():
   msg = "test"
   if request.method == 'POST':
         Username = request.form['username']
         Password = request.form['userpassword']
         Fname = request.form['userfname']
         Lname = request.form['userlname']
         Email = request.form['userEmail']
         Street = request.form['street']
         Zip = int(request.form['zip'])
         City = request.form['city']
         State = request.form['state']

         hashed = generate_password_hash(Password)
         
         conn = mysql.connect()
         cursor = conn.cursor()
         #data = cursor.fetchone()
         if not cursor is None:
            cursor.execute("SELECT * FROM user WHERE username ='" 
                    + Username + "' OR email ='" + Email + "'")
            row = cursor.fetchone ()
            if row is not None:
                flash("That Username or Email is already taken")
                return render_template('createAccount.html')
            else:
                cursor.execute("INSERT INTO user (username,password,email,fname,lname,"
                     + "street,zip,city,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                     (Username,hashed,Email,Fname,Lname,Street,Zip,City,State))
                flash ("Successfully registrated")
                conn.commit()
                #msg = "Record successfully added"
         else:
             flash ("Error during insert operation")
    
         conn.close()
         return render_template("createAccount.html")
         

@app.route('/login')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        print(e)

@app.route('/checkUser',methods = ['POST', 'GET'])
def checkUser():
    Username = request.form['username']
    Password = request.form['pass']
    
    conn = mysql.connect()
    cursor = conn.cursor()
         
    if not cursor is None:

        cursor.execute("Select password from user where username='"+Username+"'")
            
        row = cursor.fetchone ()
        if not row is None:
            hashed = row[0]
            print(hashed)
            #print(generate_password_hash(Password))
            matches = check_password_hash(hashed, Password)

            if matches:
                msg = "Login successful"
            else:
                msg = "Username or Password is wrong"
        else:
            msg = "the user is not in the database"
    conn.close()
    return render_template("result.html",msg = msg)
         

# TODO: add session behavior
@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    items = None
    form = ShoppingCart()

    if form.validate_on_submit():
        items = form.item_count.data
        form.item_count.data = 0 # Change to the updated value
        flash('Test warning message') # Really dont need this
        return redirect(url_for('shopping_cart'))
    return render_template('shopping_cart.html', form=form, item_count=items)

@app.route('/products', methods=['GET', 'POST'])
def products():
    return render_template('products.html')

@app.route('/locations')
def locations():
    try:
        storeLocations = [
                '30600 Dyer St, Union City, CA 94587', 
                'West Gate San Leandro, 1919 Davis St, San Leandro, CA 94577', 
                '40580 Albrae St, Fremont, CA 94538', 
                '777 Story rd, San Jose', 
                '301 Ranch Dr, Milpitas, CA 95035', 
                '600 Showers Dr, Mountain View, CA',
                '4080 Stevens Creek Blvd, San Jose, CA 95128', 
                'Woodside Central, 2485 El Camino Real, Redwood City, CA 94063', 
                'Bridgepointe Shopping Center, 2220 Bridgepointe Pkwy, San Mateo, CA 94404',
                '1150 El Camino Real, San Bruno, CA 94066',
                '1830 Ocean Ave, San Francisco, CA 94112',
                '2675 Geary Blvd, San Francisco, CA 94118',
                '2700 5th St, Alameda, CA 94501']
        return render_template('locations.html', key=app.config['google_maps'], storeLocations=storeLocations)
    except Exception as e:
        print(e)

@app.route('/trackDelivery')
def trackDelivery():
    try:
        items1 = ['item1', 'item2', 'item3']
        orderPlacedTime1 = datetime.strptime('2016-10-25 16:17:00', '%Y-%m-%d %H:%M:%S')
        deliveryAddress = '1 Washington Square, San Jose, CA'
        order1 = order.Order(items1, 52, orderPlacedTime1, 
                *order.getDeliveryInfo(deliveryAddress))
        #print (order1.getDeliveryStatus())
        #print (order1.getCurrentLocation())
        return render_template('map.html', key=app.config['google_maps'], order1=order1)
    except Exception as e:
        print(e)

@app.route('/listUser')
def list():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user")
    rows = cursor.fetchall(); 

    return render_template("list.html",rows = rows)
                        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
 
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
