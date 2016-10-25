from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required, NumberRange
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

# Our written additions
from settings import app_setup
from site_functions.shopping_cart import ShoppingCart


# Initialize Application
app = app_setup()
mysql = MySQL()
mysql.init_app(app)
bootstrap = Bootstrap(app)

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
             cursor.execute("INSERT INTO user (username,password,email,fname,lname,street,zip,city,state) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                     (Username,hashed,Email,Fname,Lname,Street,Zip,City,State))
             conn.commit()
             msg = "Record successfully added"
         else: 
             msg = "error in insert operation"
      
    
         conn.close()
         return render_template("result.html",msg = msg)
         

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
         

@app.route('/cart', methods=['GET', 'POST'])
def shopping_cart():
    items = None
    form = ShoppingCart()

    if form.validate_on_submit():
        items = form.item_count.data
        form.item_count.data = 0 # Change to the updated value
        session['test_session'] = 'test_session'
        return redirect(url_for('shopping_cart'))
    return render_template('shopping_cart.html', form=form, item_count=items)

@app.route('/trackDelivery')
def trackDelivery():
    key = app.config['google_maps']
    startLocation = '777 Story Rd, San Jose, CA 95122' # walmart
    endLocation = '1 Washington Sq, San Jose, CA 95192'  # SJSU
    try:
        return render_template('map.html', key=key, startLocation=startLocation, endLocation=endLocation)
    except Exception as e:
        print(e)

@app.route('/listUser')
def list():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from user")
    rows = cursor.fetchall(); 

    for row in rows:
        #rows.append(row)
        print(row)

    return render_template("list.html",rows = rows)
                        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
 
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
