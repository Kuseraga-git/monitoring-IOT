from flask import Flask, render_template, url_for, request, session
from passlib.hash import argon2
import sqlite3
import models as dbHandler

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')
app.config.from_object('secret_config')

@app.route('/', methods=['POST', 'GET'])
def index () :
        if request.method=='POST':
                login = request.form['login']
                password = request.form['password']
                users = dbHandler.retrieveUsers()
                if (argon2.verify(password, user)):
                    session['admin'] = True
                    return render_template('admin.html', users=users)
        else:
                return render_template('index.html')

@app.route('/admin/')
def admin():
    if not session:
        flash(u"Vous n'etes pas connecte", "error")
        return redirect(url_for("index"))
    elif session["admin"]:
        websites = dbHandler.retrieveUrl()
        return render_template("admin.html", websites=websites)

@app.route('/admin/add/', methods=['POST', 'GET'])
def add_website():
    if request.method == 'POST':
        url = {'url': str(request.form.get('url'))}
        dbHandler.addUrlToDb(url)
        return redirect(url_for("admin"))
    else:
        return render_template('add_website.html')

@app.route('/test/')
def blabla ():
    if not session:
        flash(u"va te pendre", "error")
        return redirect(url_for("index"))
    elif session["admin"]:
	    #return "Hello world"
	    return render_template("blabla.html")

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0')
