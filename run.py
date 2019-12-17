# -*- coding: utf-8 -*-
# encoding=utf8  
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import datetime
import os

app = Flask(__name__)

database = 'feed.db'
app.secret_key = os.urandom(24)

@app.route('/')
def index():
	conn = sqlite3.connect(database)
	c = conn.cursor()
	c.execute('select * from data order by id desc')
	result = list(c.fetchall())
	result = map(lambda x:list(x), result)
	for record in result:
		record[1] = record[1].replace('\r\n','<br>')
	return render_template('index.html', icerik=result)
	

#create
@app.route('/create', methods=['POST'])
def create():
	text = request.form['yazi']
	tarih = str(datetime.datetime.now())
	tarih = tarih[0:10]
	conn = sqlite3.connect(database)
	c = conn.cursor()
	c.execute('insert into data(icerik, tarih) values(?, ?)', (text, tarih))
	conn.commit()
	return redirect(url_for('index'))
	
	
#delete
@app.route('/delete/<int:entry_id>')
def delete(entry_id):
	#connect db
	conn = sqlite3.connect(database)
	c = conn.cursor()
	c.execute('delete from data where id = ?', [entry_id])
	conn.commit()
	return redirect(url_for('index'))
	
	
if __name__ == "__main__":
	app.run(debug=True)