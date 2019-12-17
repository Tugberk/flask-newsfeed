import sqlite3

conn = sqlite3.connect('feed.db')
print 'db opened..'
c = conn.cursor()
c.execute('create table data(ID INTEGER PRIMARY KEY AUTOINCREMENT, icerik TEXT, tarih TEXT)')	
conn.commit()