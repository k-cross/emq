from flask import Flask, render_template, request, redirect, jsonify, flash, url_for
from flask import flash, session
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm, Form
from wtforms import StringField, SubmitField, IntegerField, TextField, TextAreaField
from wtforms.validators import Required, NumberRange
from wtforms import validators, ValidationError
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    class ContactF(FlaskForm):
        fname = TextField(
            'First Name', [validators.Required("Enter your first name")])
        lname = TextField(
            'Last Name', [validators.Required("Enter your last name")])
        email = TextField('Email', [validators.Required("Enter your e-mail")])
        phone = TextField(
            'Phone Number', [validators.Required("Enter your phone number")])
        message = TextAreaField(
            'Message', [validators.Required("Enter your question")])
        submit = SubmitField("Submit")

    forms = ContactF()
    if request.method == 'POST':
        if forms.validate() == False:
            flash("Fill required fields.")
            return render_template('contact.html', forms=forms)
        else:
            flash("Sent!")
            return render_template('home.html', success=True)

    elif request.method == 'GET':
        return render_template('contact.html', forms=forms)


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

                cursor.execute(
                    "Select email,fname,lname,street,zip,city,state from user where username='" + session['username'] + "'")
                row = cursor.fetchone()

                cursor.execute(
                    "Select total_price, trans_time, status, transID from transaction where userid=%s", (session['userid']))

                orderRows = cursor.fetchall()

            conn.close()
            return render_template('profile.html', username=session['username'], email=row[0],
                                   fname=row[1], lname=row[
                                       2], street=row[3], zip=row[4],
                                   city=row[5], state=row[6], orderRows=orderRows)

        else:
            flash("Please login first!")
            return redirect(url_for('home'))

    except Exception as e:
        print(e)


@app.route('/checkUser', methods=['POST', 'GET'])
def checkUser():
    Username = request.form['username']
    Password = request.form['pass']

    conn = mysql.connect()
    cursor = conn.cursor()

    if not cursor is None:

        cursor.execute(
            "Select password,userID from user where username='" + Username + "'")

        row = cursor.fetchone()
        if not row is None:
            hashed = row[0]
            matches = check_password_hash(hashed, Password)

            if matches:
                flash("Hello, " + Username + "! Welcome!!")
                session['username'] = Username
                session['userid'] = row[1]
            else:
                flash("Username or Password is wrong")
                return render_template("login.html")
        else:
            flash("Username doesn't exist")
            return render_template("login.html")
    conn.close()
    session['usercart'] = ShoppingCart(mysql, session).cart
    return redirect(url_for('home'))


@app.route('/addUser', methods=['POST', 'GET'])
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
            row = cursor.fetchone()
            if row is not None:
                flash("That Username or Email is already taken")
                return render_template('createAccount.html')
            else:
                cursor.execute("INSERT INTO user (username,password,email,fname,lname,"
                               +
                               "street,zip,city,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (Username, hashed, Email, Fname, Lname, Street, Zip, City, State))
                flash("Successfully registrated")
                conn.commit()
        else:
            flash("Error during insert operation")

        conn.close()
        return render_template("createAccount.html")


@app.route('/updateUser', methods=['POST', 'GET'])
def updateUser():
    if request.method == 'POST':
        Fname = request.form['userfname']
        Lname = request.form['userlname']
        Street = request.form['street']
        Zip = int(request.form['zip'])
        City = request.form['city']
        State = request.form['state']

        conn = mysql.connect()
        cursor = conn.cursor()
        #data = cursor.fetchone()
        if not cursor is None:
            cursor.execute("UPDATE user SET fname=%s,lname=%s,street=%s,zip=%s,city=%s,state=%s WHERE username ='" + session['username'] + "'",
                           (Fname, Lname, Street, Zip, City, State))
            flash("Information Updated")
            conn.commit()
        else:
            flash("error in Update operation")

        conn.close()
        return redirect(url_for('profile'))


@app.route('/confirmation')
def order_confirmation():
    # Need to handle true validation / or we just assume it works and outside
    # our scope
    return render_template('order_confirmation.html')


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' in session:
        form = CheckoutForm()
        if session['total'] == 0:
            flash("No item in the shopping cart")
            return redirect(url_for('shopping_cart'))
        
        if 'usercart' not in session:
            return redirect(url_for('shopping_cart'))

        if form.validate_on_submit():
            cc = form.credit_card.data
            ct = form.card_type.data

            # TODO: Replace with shopping cart function logic
            if not ShoppingCart(mysql, session).checkout():
                flash("The address must within the bay area")
                return redirect(url_for('shopping_cart'))

            return redirect(url_for('order_confirmation'))
        return render_template('checkout.html', form=form, total=session['total'])
    else:
        return redirect(url_for('login'))


@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():

    conn = mysql.connect()
    cursor = conn.cursor()

    if 'username' in session:
        usercart = ShoppingCart(mysql, session)
        form = usercart.form
        session['usercart'] = usercart.cart
        cart = session['usercart']

        #update quantity
        if request.method == 'POST':
            #checkout 
            if form.validate_on_submit():
                print("66")
                if form.checkout_btn.data:
                    session['total'] = usercart.calculate_total()[0]
                    return redirect(url_for('checkout'))
            else:
                quantity = request.form['quantity']
                i = request.form['id']
                print(i+" "+quantity)
                usercart.update_cart(cart[int(i)-1][1], quantity)    
                return redirect(url_for('shopping_cart'))        

        return render_template('shopping_cart.html', form=form,
                               total=usercart.calculate_total(), cart=cart, count=0)
    else:
        flash('Please Login')
        return redirect(url_for('login'))


# TODO: Implement a dynamic product page
@app.route('/products', methods=['GET', 'POST'])
def products():
    cursor = mysql.connect().cursor()
    if request.method == 'POST':
        searchTerm = request.form['search'].strip()
        queryTerm = '\'%' + searchTerm + '%\''       
        query = ("select I.*, SUM(I_D.stock) from inventory I, inventory_details I_D where I.pID = I_D.pID and pname like %s group by I.pID" % queryTerm)
        cursor.execute(query)
    else:
        cursor.execute("select I.*, SUM(I_D.stock) from inventory I, inventory_details I_D where I.pID = I_D.pID group by I.pID") 
    rows = cursor.fetchall()    
    return render_template('products.html', products = rows)


@app.route('/about')
def locations():
    cursor = mysql.connect().cursor()
    cursor.execute(
        "select  CONCAT(store.street, ', ', store.city, ', ', store.state, ' ', store.zip) as storeAddress from store")
    rows = cursor.fetchall()
    return render_template('locations.html', key=app.config['google_maps'], storeLocations=rows)


@app.route('/trackDelivery/', methods=['GET', 'POST'])
def trackDelivery():
    try:
        transID = request.form['track']
        order1 = order.Order(transID)
        return render_template('map.html', key=app.config['google_maps'], order1=order1)
    except Exception as e:
        print(e)


@app.route('/sproduct', methods=['GET', 'POST'])
def singleproduct():
    try:
        pID = request.args.get('id')
        cursor = mysql.connect().cursor()
        cursor.execute("select I.* from inventory I where I.pID =" + str(pID))
        row = cursor.fetchone()
        print (cursor.rowcount)
        if(cursor.rowcount != 0):
            cursor.execute("select I.*, SUM(I_D.stock) from inventory I, inventory_details I_D where I.pID = I_D.pID and I.pID =" + str(pID))
            row = cursor.fetchone()
            return render_template('singleproduct.html', product=row)
        else:
            return render_template('product_not_exist.html')
    except Exception as e:
        print(e)


@app.route('/product/<int:id>', methods=['GET', 'POST'])
def product(id):
    
    if 'username' in session:
       
        #add from Single product page
        if request.method == 'POST':
            
            product_Quantity = request.form['product-quantity-input']
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM cart WHERE pID = %s AND username = %s",
                           (id, session['username']))
            row = cursor.fetchone()

            if row is None:
                
                cursor.execute("INSERT INTO cart (username, pID, quantity) VALUES (%s, %s, %s)",
                               (session['username'], id, product_Quantity))
                conn.commit()
                conn.close()
                flash("New item is added to cart")
                return redirect(url_for('products'))

            else:
                
                cursor.execute("SELECT quantity FROM cart WHERE pID = %s", (id))
                row = cursor.fetchone()
                
                quantity = row[0]
                quantity = quantity + int(product_Quantity)

                cursor.execute("UPDATE cart SET quantity=%s WHERE pID = %s", (quantity, id))
                conn.commit()
                conn.close()
                flash("Seleted item is increaed by "+ product_Quantity)
                return redirect(url_for('products'))
        else:
            
            print("testingtesting")
            #add from products page
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM cart WHERE pID = %s AND username = %s",
                               (id, session['username']))
            row = cursor.fetchone()

            if row is None:
                cursor.execute("INSERT INTO cart (username, pID, quantity) VALUES (%s, %s, %s)",
                               (session['username'], id, 1))
                conn.commit()
                conn.close()
                flash("New item is added to cart")
                return redirect(url_for('products'))

            else:
                cursor.execute("SELECT quantity FROM cart WHERE pID = %s", (id))
                row = cursor.fetchone()
                
                quantity = row[0]
                quantity = quantity + 1

                cursor.execute("UPDATE cart SET quantity=%s WHERE pID = %s", (quantity, id))
                conn.commit()
                conn.close()
                flash("Seleted item is increaed by 1")
                return redirect(url_for('products'))
            
    else:
        flash("Please Login First")
        return redirect(url_for('products'))
 


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
