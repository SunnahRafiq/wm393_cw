from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        name=request.form['uname']
        password=request.form['psw']
        query="SELECT name,password FROM users where name ='"+name+"' and password='"+password+"'"
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

if __name__ == "__main__":
  app.run(debug=True)
