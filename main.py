from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route("/")
def login():
  return render_template('login.html')
@app.route("/register")
def register():
  return render_template('register.html')
@app.route('/landing')
def landing():
  return render_template('landing.html')

if __name__ == "__main__":
  app.run(debug=True)
