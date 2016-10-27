from flask import Flask, render_template, redirect, url_for, request
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/createAccount' , methods = ['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('createAccount.html')
	user = User(request.form['fname'], request.form['lname'], request.form['email'], 
		request.form['phone'], request.form['username'], request.form['password'])
	#add user to data base
	#commit to db
	return redirect(url_for('login')) #Create page to initiate login/registered

@app.route('/login' , methods = ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	return redirect(url_for('index'))
