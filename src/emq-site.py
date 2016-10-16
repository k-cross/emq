from flask import Flask
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

@app.route('/')
def rootRedirect():
    return redirect('/home')

@app.route('/home')
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

@app.route('/cart')
def shopping_cart():
    try:
        return render_template('shopping_cart.html')
    except Exception as e:
        # Probably better to log exceptions rather than print them
        print(e)

@app.route('/trackDelivery')
def trackDelivery():
    key = 'AIzaSyB7BkwSe4-5V14C3wY301HVolGN2IdO2PA'
    startLocation = '777 Story Rd, San Jose, CA 95122' # walmart
    endLocation = '1 Washington Sq, San Jose, CA 95192'  # SJSU
    try:
        return render_template('map.html', key=key, startLocation=startLocation, endLocation=endLocation)

    except Exception as e:
        print(e)

 
if __name__ == '__main__':
    app.run(debug=True)
