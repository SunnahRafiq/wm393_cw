from flask import Flask, render_template,request
import sqlite3

import users

app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        name=request.form['uname']
        password=request.form['psw']
        query="SELECT username,password FROM users where username ='"+name+"' and password='"+password+"'"
        cur.execute(query)
        results=cur.fetchall()
        if len(results)==0:
            print('SORRY INCORRECT CREDENTIALS TRY AGAIN')
        else:
            return render_template('landing.html')
    return render_template('login.html')

@app.route("/register")
def register():
  return render_template('register.html')
@app.route('/landing')
def landing():
  return render_template('landing.html')
@app.route('/statistic')
def statistic():
    students=users.get_students()
    return render_template('statistic.html',students=students)
@app.route('/permission')
def permission():
  return render_template('permission.html')
@app.route('/account')
def account():
  return render_template('account.html')
@app.route('/logout')
def logout():
  return render_template('logout.html')
if __name__ == "__main__":
  app.run(debug=True)

