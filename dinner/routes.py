#from dinner import dinner
import os
import sys
import json
import request
from flask import Flask, request, jsonify, render_template, flash, redirect, session, url_for, make_response
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm


CORS(dinner)
dinner.secret_key = 'yoг newer newer newer newer newer now this secret key'
application = dinner

mysql = MySQL()
dinner.config['MYSQL_DATABASE_USER'] = 'cp36696_admireso'
dinner.config['MYSQL_DATABASE_PASSWORD'] = 'social.admire'
dinner.config['MYSQL_DATABASE_DB'] = 'cp36696_admireso'
dinner.config['MYSQL_DATABASE_HOST'] = 'localhost'
dinner.config['UPLOAD_FOLDER'] = "/home/c/cp36696/dinner_near/public_html/dinner/images"
mysql.init_app(dinner)

conn = mysql.connect()
cursor = conn.cursor()

@dinner.route('/index')
def hello_world():
    return 'здарова мир'
    
@dinner.route('/database/point_add', methods=['POST'])
def data_load():
	data = request.data
	json = eval(data)
	title = str(json["title"])
	description = str(json["description"])
	images = str(json["images"])
	price = str(json["price"])
	FIO = str(json["FIO"])
	lat = str(json["lat"])
	longi = str(json["long"])
	cursor.execute("insert into dinner_near (title, description, images, price, FIO, latitude, longitude) values ('" + title + "','"  + description + "','" + images + "','" + price + "','" + FIO + "','" + lat + "','" + longi + "')")
	conn.commit()
	conn.close()
	return make_response("", 200)
	
@dinner.route('/database/point_view/<ID>', methods=['GET'])
def data_view(ID):
	check_summ = 0
	cursor.execute("SELECT * FROM dinner_near WHERE id IN (" + ID + ")")
	res = cursor.fetchone()
	if res is not None:
		View = res
	json = {"id" : View[0],
		"title" : View[1],
        "description" : View[2],
        "images" :  View[3],
        "price" : View[4],
        "FIO" : View[5],
        "lat" : View[6],
        "long" : View[7]}
	return jsonify(json)

@dinner.route('/regist', methods=['POST'])
def regist():
	data = request.data
	json = eval(data)
	email = str(json["email"])
	password = str(json["password"])
	create_time = str(json["create_time"])
	pasport_number = str(json["pasport_number"])
	birthday_date = str(json["birthday_date"])
	pasport_photo = str(json["pasport_photo"])
	avatar = str(json["avatar"])
	sex = str(json["sex"])
	fio = str(json["fio"])
	miting = str(0)
	cursor.execute("SELECT * FROM dinner_users WHERE email = %s", (email))
	check = cursor.fetchone()
	if check == None:
		cursor.execute("insert into dinner_users (email, password, create_time, pasport_number, birthday_date, pasport_photo, avatar, sex, FIO, miting_count) values ('" + email + "','"  + password + "','" + create_time + "','" + pasport_number + "','" + birthday_date + "','" + pasport_photo + "','" + avatar + "','" + sex + "','" + fio + "','" + miting + "')")
		conn.commit()
		conn.close()
		return make_response("", 200)
	else:
		return make_response("", 500)
	
@dinner.route('/login', methods=['GET', 'POST'])
def login():
	data = request.data
	json = eval(data)
	email = str(json["email"])
	password = str(json["password"])
	cursor.execute('SELECT * FROM dinner_users WHERE email = %s AND password = %s', (email, password))
	account = cursor.fetchone()
	if account:
		return make_response("", 200)
	else:
		return make_response("", 500)

