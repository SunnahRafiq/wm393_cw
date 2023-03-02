from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from users import Users
from mystat import Statistic

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
    students=Users.get_students()
    return render_template('statistic.html',students=students)


@app.route('/statistic/<username>')
def stat_detail(username):
    attendance, quiz_submissions, tutor_engagement = Statistic.get_statistic(username)
    user = Users(username, None, 'student')
    user.attendance = attendance
    user.quiz_submissions = quiz_submissions
    user.tutor_engagement = tutor_engagement
    return render_template('stat_detail.html', user=user)


@app.route('/permission', methods=['GET', 'POST'])
@app.route('/permission/<username>', methods=['GET', 'POST'])
def permission(username=None):
    if request.method == 'POST':
        flash('Permissions updated successfully', 'success')
        return redirect(url_for('permission'))

    users = Users.get_students()
    return render_template('permission.html', users=users, username=username)

@app.route('/update_permission/<username>', methods=['POST'])
def update_permission(username):
    return redirect(url_for('permission', username=username))


@app.route('/account')
def account():
  return render_template('account.html')


@app.route('/logout')
def logout():
  return render_template('logout.html')


if __name__ == "__main__":
  app.run(debug=True)

