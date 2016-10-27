from flask import Flask, render_template, redirect, url_for, request
from flask.ext.login import login_user, logout_user, current_user, login_required

@app.route('/')
@login_required
def index():


@app.route('/login', methods=['GET', 'POST'])
def login():
		if request.method == 'GET':
				return render_template("login.html")
			user = request.form['username']
			passw = request.form['password']

			
			
			
			isRegistered = User.query.filter_by(user = username, passw = password).first()
			if(isRegisered is none)
				flash('Incorrect login. Please try again')
				return redirect(url_for('login'))
			login(isRegistered) #Logged in
			flash('Successfully logged in.')
			return redirect(url_for('index'))							
		#return render_template('login.html', loginError = loginError)		

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


