from flask import Flask, render_template, request, redirect, jsonify, flash, url_for
from flask import flash, session
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
from site_functions.shopping import ShoppingCart, CheckoutForm
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


@app.route('/login')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        print(e)


@app.route('/logout')
def logout():
    try:
        if 'username' in session:
            session.pop('username', None)
            session.pop('userid', None)
            return render_template('login.html')
        else:
            flash("Please login first!")
            return redirect(url_for('home'))
    except Exception as e:
        print(e)


@app.route('/profile')
def profile():
    try:
        if 'username' in session:
            conn = mysql.connect()
            cursor = conn.cursor()
                 
            if not cursor is None:

                cursor.execute("Select email,fname,lname,street,zip,city,state from user where username='"+session['username']+"'")
                    
                row = cursor.fetchone ()
                
            conn.close()
            return render_template('profile.html',username=session['username'], email=row[0], fname=row[1], lname=row[2], street=row[3], zip=row[4], city=row[5], state=row[6])     

        else:
            flash("Please login first!")
            return redirect(url_for('home'))

    except Exception as e:
        print(e)


@app.route('/checkUser',methods = ['POST', 'GET'])
def checkUser():
    Username = request.form['username']
    Password = request.form['pass']
    
    conn = mysql.connect()
    cursor = conn.cursor()
         
    if not cursor is None:

        cursor.execute("Select password,userID from user where username='"+Username+"'")
            
        row = cursor.fetchone ()
        
        if not row is None:
            hashed = row[0]
            print(hashed)
            matches = check_password_hash(hashed, Password)

            if matches:
                flash("Hello, "+Username+"! Welcome!!")
                session['username'] = Username
                session['userid'] = row[1]
                print(session['username'],session['userid'])
            else:
                flash("Username or Password is wrong")
                return render_template("login.html")
        else:
            flash("UserName doesn't exist")
            return render_template("login.html")
    conn.close()
    return redirect(url_for('home'))


@app.route('/addUser',methods = ['POST', 'GET'])
def addUser():
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
         else:
             flash ("Error during insert operation")
    
         conn.close()
         return render_template("createAccount.html")


@app.route('/updateUser',methods = ['POST', 'GET'])
def updateUser():
   if request.method == 'POST':
         Fname = request.form['userfname']
         Lname = request.form['userlname']
         Street = request.form['street']
         Zip = int(request.form['zip'])
         City = request.form['city']
         State = request.form['state']
         print(Fname,Lname,Street,Zip,City,State)
           
         conn = mysql.connect()
         cursor = conn.cursor()
         #data = cursor.fetchone()
         if not cursor is None:
            cursor.execute("UPDATE user SET fname=%s,lname=%s,street=%s,zip=%s,city=%s,state=%s",
                     (Fname,Lname,Street,Zip,City,State))
            flash ("Information Updated")
            conn.commit()
         else:
            flash ("error in Update operation")
            
         conn.close()
         return redirect(url_for('profile'))


@app.route('/confirmation')
def order_confirmation():
    # Need to handle true validation / or we just assume it works and outside our scope
    return render_template('order_confirmation.html')


#TODO: complete function / currently broken
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' in session:
        form = CheckoutForm()

        if form.validate_on_submit():
            connection = mysql.connect()
            cursor = connection.cursor()

            # TODO: Replace with shopping cart function logic
            cursor.execute(information_query.format(session['username']))

            cc = form.credit_card.data
            ct = form.card_type.data

            # TODO: Replace with shopping cart function logic
            cursor.execute(transaction_query.format(session['userid'], 
                session['total'], 'Pending'))
            cursor.commit()
            connection.close()

            return redirect(url_for('shopping_cart'))
        return render_template('checkout.html', form=form)
    else:
        return redirect(url_for('login'))


#TODO: Redirect to checkout when complete
@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    items = None
    cart = ShoppingCart(mysql, session)
    form = cart.form

    if form.validate_on_submit():
        print(cart.calculate_total())
        return redirect(url_for('shopping_cart'))
    return render_template('shopping_cart.html', form=form)


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
