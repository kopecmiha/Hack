from dinner import dinner
import os
import time
import base64
import sys
import json
import random
import request
from flask import Flask, request, jsonify, render_template, flash, redirect, session, url_for, make_response, send_from_directory
from flask_cors import CORS
from flaskext.mysql import MySQL
from flask_wtf import FlaskForm




application = dinner
dinner.secret_key = 'yoг newer newer newer newer newer now this secret key'
mysql = MySQL()
dinner.config['MYSQL_DATABASE_USER'] = 'cp36696_admireso'
dinner.config['MYSQL_DATABASE_PASSWORD'] = 'social.admire'
dinner.config['MYSQL_DATABASE_DB'] = 'cp36696_admireso'
dinner.config['MYSQL_DATABASE_HOST'] = 'localhost'
dinner.config['UPLOAD_FOLDER'] = "/home/c/cp36696/dinner_near/public_html/dinner/images"
mysql.init_app(dinner)
CORS(dinner)
conn = mysql.connect()
cursor = conn.cursor()
    
@dinner.route('/database/point_add', methods=['POST'])
def data_load():
	check = 0
	path_list = ""
	data = request.data
	json = eval(data)
	title = str(json["title"])
	description = str(json["description"])
	images = json["images"]
	for i in images:
		img = base64.b64decode(i)
		path = r"home/c/cp36696/dinner_near/public_html"
		path_wr = r"/dinner/images/image_point" + str(time.time()) + str(random.randint(0, 999)) + ".png"
		with open(path + path_wr, "wb") as image_file:
			image_file.write(img)
			path_list += (r"http://dinner-near.tw1.ru" + path_wr + "::")
	price = str(json["price"])
	User_ID = str(json["User_ID"])
	lat = str(json["lat"])
	longi = str(json["long"])
	address = str(json["address"])
	cursor.execute("SELECT place_count FROM dinner_users WHERE id IN (" + User_ID + ")")
	(check,) = cursor.fetchone()
	if check == 1:
		active = str(0)
		cursor.execute("SELECT active FROM dinner_near WHERE User_ID IN (" + User_ID + ")")
		(active,) = cursor.fetchone()
		cursor.execute("DELETE FROM dinner_near WHERE User_ID = " + User_ID)
		conn.commit()
		cursor.execute("insert into dinner_near (title, description, images, price, User_ID, latitude, longitude, address, active) values ('" + title + "','"  + description + "','" + path_list +  "','" + price + "','" + User_ID + "','" + lat + "','" + longi + "','" + address + "','" + str(active) + "')")
		conn.commit()
	else:
		cursor.execute("insert into dinner_near (title, description, images, price, User_ID, latitude, longitude, address) values ('" + title + "','"  + description + "','" + path_list +  "','" + price + "','" + User_ID + "','" + lat + "','" + longi + "','" + address + "')")
		cursor.execute("UPDATE dinner_users SET place_count = %s WHERE id IN (" + User_ID + ")", (1))
		conn.commit()
	conn.close()
	return make_response("", 200)
	#return str(check)

	
@dinner.route('/database/point_view/<ID>', methods=['GET'])
def data_view(ID):
	check_summ = 0
	json2 = None
	cursor.execute("SELECT * FROM dinner_near WHERE id IN (" + ID + ")")
	res = cursor.fetchone()
	if res is not None:
		View = res
		User_ID = str(View[3])
		cursor.execute("SELECT * FROM dinner_users WHERE id IN (" + User_ID + ")")
		User = cursor.fetchone()
		if User is not None:
			View2 = User
			json2 = {"id" : View2[0],
				"email" : View2[1],
        		"create_time" : View2[3],
        		"pasport_number" :  View2[4],
        		"birthday_date" : View2[5],
        		"pasport_photo" : View2[6],
        		"avatar" : View2[7],
        		"sex" : View2[8],
        		"FIO" : View2[9],
				"miting_count" : View2[10],
				"place_count" : View2[11]
				}
		json = {"id" : View[0],
				"title" : View[1],
        		"description" : View[2],
        		"User" :  json2,
        		"price" : View[4],
        		"lat" : View[5],
        		"long" : View[6],
        		"images" : View[7],
        		"address" : View[8]}
	else:
		json = None
	conn.close()
	return jsonify(json)
	
@dinner.route('/database/user_view/<ID>', methods=['GET'])
def user_view(ID):
	check_summ = 0
	cursor.execute("SELECT * FROM dinner_users WHERE id IN (" + ID + ")")
	res = cursor.fetchone()
	if res is not None:
		View = res
		json = {"id" : View[0],
				"email" : View[1],
        		"create_time" : View[3],
        		"pasport_number" :  View[4],
        		"birthday_date" : View[5],
        		"pasport_photo" : View[6],
        		"avatar" : View[7],
        		"sex" : View[8],
        		"FIO" : View[9],
				"miting_count" : View[10],
				"place_count" : View[11],
				"desription" : View[12]
		}
	else:
		json = None
	conn.close()
	return jsonify(json)
	
@dinner.route('/database/point_view_all', methods=['GET'])
def all_view():
	cursor.execute("SELECT count(*) FROM dinner_near")
	count = int(cursor.fetchone()[0])
	arr = []
	User = None
	for i in range(0,count):
		cursor.execute("SELECT * FROM dinner_near WHERE active = 1 LIMIT %s, 1", (i))
		View = cursor.fetchone()
		if View:
			User_ID = str(View[3])
			cursor.execute("SELECT * FROM dinner_users WHERE id IN (" + User_ID + ")")
			User = cursor.fetchone()
			if User is not None:
				View2 = User
				json2 = {"id" : View2[0],
					"email" : View2[1],
        			"create_time" : View2[3],
        			"pasport_number" :  View2[4],
        			"birthday_date" : View2[5],
        			"pasport_photo" : View2[6],
        			"avatar" : View2[7],
        			"sex" : View2[8],
        			"FIO" : View2[9],
					"miting_count" : View2[10],
					"place_count" : View2[11]
					}
			json = {"id" : View[0],
				"title" : View[1],
        		"description" : View[2],
        		"User" :  json2,
        		"price" : View[4],
        		"lat" : View[5],
        		"long" : View[6],
        		"images" : View[7],
        		"address" : View[8]}
			arr.append(json)
	conn.close()
	return jsonify(arr)
	
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
	pasport_photo = base64.b64decode(pasport_photo)
	desc = str(json["description"])
	avatar = str(json["avatar"])
	avatar = base64.b64decode(avatar)
	sex = str(json["sex"])
	fio = str(json["fio"])
	miting = str(0)
	cursor.execute("SELECT * FROM dinner_users WHERE email = %s", (email))
	check = cursor.fetchone()
	if check == None:
		path = r"home/c/cp36696/dinner_near/public_html"
		path_wr = r"/dinner/images/image" + str(time.time()) + str(random.randint(0, 999)) + ".png"
		path_av = r"home/c/cp36696/dinner_near/public_html"
		path_av_wr = r"/dinner/images/image_av" + str(time.time()) + str(random.randint(0, 999)) + ".png"
		with open(path + path_wr, "wb") as image_file:
			image_file.write(pasport_photo)
		with open(path_av + path_av_wr, "wb") as image_file_av:
			image_file_av.write(avatar)
		cursor.execute("insert into dinner_users (email, password, create_time, pasport_number, birthday_date, pasport_photo, avatar, sex, FIO, miting_count, description) values ('" + email + "','"  + password + "','" + create_time + "','" + pasport_number + "','" + birthday_date + "','" + r"http://dinner-near.tw1.ru" + path_wr + "','" + r"http://dinner-near.tw1.ru" + path_av_wr + "','" + sex + "','" + fio + "','" + miting + "','" + desc + "')")
		conn.commit()
		conn.close()
		return make_response("", 200)
	else:
		return make_response("email error", 500)
	
@dinner.route('/user_update', methods=['POST'])
def update():
	data = request.data
	json = eval(data)
	ID = str(json["id"])
	email = str(json["email"])
	password = str(json["password"])
	create_time = str(json["create_time"])
	pasport_number = str(json["pasport_number"])
	birthday_date = str(json["birthday_date"])
	pasport_photo = str(json["pasport_photo"])
	avatar = str(json["avatar"])
	sex = str(json["sex"])
	fio = str(json["fio"])
	miting = str(json["miting_count"])
	if email != "":
		cursor.execute("UPDATE dinner_users SET email = %s WHERE id IN (%s)", (email, ID))
		conn.commit()
	if password != "":
		cursor.execute("UPDATE dinner_users SET password = %s WHERE id IN (%s)", (password, ID))
		conn.commit()
	if pasport_number != "":
		cursor.execute("UPDATE dinner_users SET pasport_number = %s WHERE id IN (%s)", (pasport_number, ID))
		conn.commit()
	if birthday_date != "":
		cursor.execute("UPDATE dinner_users SET birthday_date = %s WHERE id IN (%s)", (birthday_date, ID))
		conn.commit()
	if pasport_photo != "":
		cursor.execute("UPDATE dinner_users SET pasport_photo = %s WHERE id IN (%s)", (pasport_photo, ID))
		conn.commit()
	if avatar != "":
		cursor.execute("UPDATE dinner_users SET avatar = %s WHERE id IN (%s)", (avatar, ID))
		conn.commit()
	if sex != "":
		cursor.execute("UPDATE dinner_users SET sex = %s WHERE id IN (%s)", (sex, ID))
		conn.commit()
	if fio != "":
		cursor.execute("UPDATE dinner_users SET FIO = %s WHERE id IN (%s)", (fio, ID))
		conn.commit()
	if miting != "":
		cursor.execute("UPDATE dinner_users SET miting_count = %s WHERE id IN (%s)", (miting, ID))
		conn.commit()
	conn.close()
	return make_response("", 200)
	
@dinner.route('/login', methods=['POST'])
def login():
	data = request.data
	json = eval(data)
	email = str(json["email"])
	password = str(json["password"])
	cursor.execute('SELECT id FROM dinner_users WHERE email = %s AND password = %s', (email, password))
	(account,) = cursor.fetchone()
	if account:
		#return make_response("", 200)
		conn.close()
		return str(account)
	else:
		conn.close()
		return make_response("error", 500)

@dinner.route('/status', methods=['POST'])
def status():
	data = request.data
	json = eval(data)
	User_ID = str(json["User_ID"])
	status = str(json["status"])
	cursor.execute('UPDATE dinner_near Set active = %s WHERE User_ID = %s', (status, User_ID))
	conn.commit()
	conn.close()
	return make_response("", 200)
	
@dinner.route('/user_desc', methods=['POST'])
def user_desc():
	data = request.data
	json = eval(data)
	ID = str(json["id"])
	desc = str(json["description"])
	cursor.execute('UPDATE dinner_users Set description = %s WHERE id = %s', (desc, ID))
	conn.commit()
	conn.close()
	return make_response("", 200)
	
@dinner.route('/user_id_status/<ID>', methods=['GET'])
def user_id_status(ID):
	User_ID = ID
	cursor.execute('SELECT active FROM dinner_near WHERE User_ID = %s', (User_ID))
	conn.commit()
	conn.close()
	return jsonify(cursor.fetchone())
	
@dinner.route('/')
def index():
	return render_template('index.html')
	
@dinner.errorhandler(404)
def not_found_error(error):
	return redirect("/")


@dinner.route('/js/<path:path>')
def send_js(path):
	return send_from_directory(r'templates/js', path)

@dinner.route('/fonts/<path:path>')
def send_fonts(path):
	return send_from_directory(r'templates/fonts', path)

@dinner.route('/css/<path:path>')
def send_css(path):
	return send_from_directory(r'templates/css', path)
	
@dinner.route('/img/<path:path>')
def send_img(path):
	return send_from_directory(r'templates/img', path)
	
@dinner.route('/<path:path>')
def send_ico(path):
	return send_from_directory(r'templates/', path)
