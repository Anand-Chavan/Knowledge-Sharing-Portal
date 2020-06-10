import flask
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

# def mysql_config():
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'newuser'
app.config['MYSQL_PASSWORD'] = 'Sur78anand@#'
app.config['MYSQL_DB'] = 'anand'

mysql = MySQL(app)
