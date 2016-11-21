from flask import Flask, render_template, request, redirect, url_for
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
from ..settings import app_setup
from ..site_functions.shopping import ShoppingCart, CheckoutForm, ShoppingCartButtonForm
from ..site_functions import order

# Initialize Application
#app = app_setup()
#mysql = MySQL()
#mysql.init_app(app)
#bootstrap = Bootstrap(app)
#moment = Moment(app)


@main.route('/')
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        print(e)


@main.route('/createAccount')
def createAccount():
    try:
        return render_template('createAccount.html')
    except Exception as e:
        print(e)


@main.route('/login')
def login():
    try:
        return render_template('login.html')
    except Exception as e:
        print(e)


@main.route('/logout')
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


@main.route('/profile')
def profile():
    try:
        if 'username' in session:
            conn = mysql.connect()
            cursor = conn.cursor()
                 
            if not cursor is None:

                cursor.execute("Select email,fname,lname,street,zip,city,state from user where username='"+session['username']+"'")  
                row = cursor.fetchone ()

                cursor.execute("Select total_price, trans_time, status, transID from transaction where userid=%s",(session['userid']))
                orderRows = cursor.fetchall()
                
            conn.close()
            return render_template('profile.html',username=session['username'], email=row[0],
                                   fname=row[1], lname=row[2], street=row[3], zip=row[4],
                                   city=row[5], state=row[6],orderRows = orderRows)     

        else:
            flash("Please login first!")
            return redirect(url_for('home'))

    except Exception as e:
        print(e)


@main.route('/checkUser',methods = ['POST', 'GET'])
def checkUser():
    Username = request.form['username']
    Password = request.form['pass']
    
    conn = mysql.connect()
    cursor = conn.cursor()
         
    if not cursor is None:

        cursor.execute("Select password,userID from user where username='"+Username+"'")
            
        row = cursor.fetchone ()
        print(row)
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
    session['usercart'] = ShoppingCart(mysql, session).cart
    return redirect(url_for('home'))


@main.route('/addUser',methods = ['POST', 'GET'])
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
                flash ("Successfully Registered")
                conn.commit()
         else:
             flash ("Insertion Error")
    
         conn.close()
         return render_template("createAccount.html")


@main.route('/updateUser',methods = ['POST', 'GET'])
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
         if not cursor is None:
            cursor.execute("UPDATE user SET fname=%s,lname=%s,street=%s,zip=%s,city=%s,state=%s WHERE username ='"+session['username']+"'",
                     (Fname,Lname,Street,Zip,City,State))
            flash ("Information Updated")
            conn.commit()
         else:
            flash ("error in Update operation")
            
         conn.close()
         return redirect(url_for('profile'))


@main.route('/confirmation')
def order_confirmation():
    # Need to handle true validation / or we just assume it works and outside our scope
    return render_template('order_confirmation.html')


@main.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' in session:
        form = CheckoutForm()

        if 'usercart' not in session:
            return redirect(url_for('shopping_cart'))

        if form.validate_on_submit():
            cc = form.credit_card.data
            ct = form.card_type.data

            # TODO: Replace with shopping cart function logic
            ShoppingCart(mysql, session).checkout()

            return redirect(url_for('order_confirmation'))
        return render_template('checkout.html', form=form, total=session['total'])
    else:
        return redirect(url_for('login'))


@main.route('/cart', methods=['GET', 'POST'])
def shopping_cart():

    conn = mysql.connect()
    cursor = conn.cursor()

    
    if 'username' in session:
        usercart = ShoppingCart(mysql, session)
        form = usercart.form
        session['usercart'] = usercart.cart
        cart=session['usercart']
        
        item_forms = usercart.item_forms
        print(item_forms)
        if form.validate_on_submit():
            if form.checkout_btn.data:
                session['total'] = usercart.calculate_total()[0]
                return redirect(url_for('checkout'))
            else:
                # TODO: Implement update 
##                for i in range(0, len(cart)):
##                    string = str(i)
##                    item = item_forms[i].update_btn
##                    #item = request.args.get(string)
##                    print(item.data)
##                    cursor.execute("UPDATE cart SET quantity =%s WHERE pID=%s",
##                     (item, 1))
##                    conn.commit()
##                flash ("Cart Updated")
##                conn.close()
                
                return redirect(url_for('shopping_cart'))
        return render_template('shopping_cart.html', form=form, 
                total=usercart.calculate_total(), item_forms=item_forms, cart=cart, count=0)
    else:
        flash('Please Login')
        return redirect(url_for('login'))


# TODO: Implement a dynamic product page
@main.route('/products', methods=['GET', 'POST'])
def products():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM inventory") 
    rows = cursor.fetchall()    
    return render_template('products.html', products = rows)


@main.route('/locations')
def locations():
    cursor = mysql.connect().cursor()
    cursor.execute("select  CONCAT(store.street, ', ', store.city, ', ', store.state, ' ', store.zip) as storeAddress from store") 
    rows = cursor.fetchall()
    return render_template('locations.html', key=main.config['google_maps'], storeLocations=rows)


@main.route('/trackDelivery/', methods=['GET', 'POST'])
def trackDelivery():
    try:
        transID = request.form['track']
        order1 = order.Order(transID)
        return render_template('map.html', key=main.config['google_maps'], order1=order1)
    except Exception as e:
        print(e)


@main.route('/sproduct', methods=['GET', 'POST'])
def singleproduct():
    try:
        pID = request.args.get('id')
        cursor = mysql.connect().cursor()
        cursor.execute("select * from inventory where pID =" + str(pID)) 
        row = cursor.fetchone()   
        return render_template('singleproduct.html', product = row)
    except Exception as e:
        print(e)
        

@main.route('/product/<int:id>')
def product(id):
    if 'username' in session:
        conn = mysql.connect()
        cursor = conn.cursor()
        print(id)
        
        cursor.execute("SELECT * FROM cart WHERE pID = %s AND username = %s",
                (id,session['username']))
        row = cursor.fetchone ()
        
        if row is None:
            cursor.execute("INSERT INTO cart (username, pID, quantity) VALUES (%s, %s, %s)",
                           (session['username'], id, 1))
            conn.commit()
            conn.close()
            flash("New item is added to cart")
            return redirect(url_for('products'))

        else:
            cursor.execute("SELECT quantity FROM cart WHERE pID = %s",(id))
            row = cursor.fetchone ()

            quantity = row[0]
            quantity = quantity +1
            
            cursor.execute("UPDATE cart SET quantity=%s WHERE pID = %s",(quantity, id))
            conn.commit()
            conn.close()
            flash("Seleted is increaed by one")
            return redirect(url_for('products'))
    else:
        flash("Please Login First")
        return redirect(url_for('products'))
        

@main.route('/listUser')
def list():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from orders")
    rows = cursor.fetchall(); 

    return render_template("list.html",rows = rows)
                        

if __name__ == '__main__':
    main.run(host='0.0.0.0')