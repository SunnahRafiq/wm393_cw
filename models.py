import sqlite3

def loginUser():
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    com= "CREATE TABLE IF NOT EXISTS users(user_id integer primary key autoincrement,name text,password text)"
    cur.execute(com)

def insertUser(username,password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users