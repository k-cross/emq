from flask import Flask, render_template, request, redirect, jsonify

def app_setup():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test' # This really should go in a seperate file

    #change user and password if needed
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'emq'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    return app
