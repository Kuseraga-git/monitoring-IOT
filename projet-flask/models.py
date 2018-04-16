import sqlite3 as sql

def retrieveUsers():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT login, password FROM Users")
    users = cur.fetchall()
    con.close()
    return users

def retrieveUrl():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT url, response, date FROM Websites, Response WHERE Websites.id = Responses.id_url ORDER BY date DESC")
	sites = cur.fetchall()
	con.close()
	return sites

def addUrlToDb(urlToAdd):
	con = sql.connect("database.db")
	cur.con.cursor()
	cur.execute("INSERT INTO Websites (url) VALUES (%(urlToAdd)s)", urlToAdd)
	con.commit()
	con.close()