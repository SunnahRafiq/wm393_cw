from flask import Flask, render_template, request, redirect, url_for, flash, session,g
import sqlite3
from users import Users
from mystat import Statistic
from admin import Admin

app = Flask(__name__)
app.secret_key = 'secret'


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
            session['username'] = name  # Store the username in the session object
            return redirect(url_for('landing'))
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route('/landing')
def landing():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('landing.html')


@app.route('/statistic')
@app.route('/statistic/<username>')
def statistic(username=None):
    if username is None:
        if 'username' not in session:
            return redirect(url_for('login'))
        username = session['username']
    students = Users.get_user()
    attendance, quiz_submissions, tutor_engagement = Statistic.get_statistic(username)
    user = Users(username, None, 'student', None, None)
    user.attendance = attendance
    user.quiz_submissions = quiz_submissions
    user.tutor_engagement = tutor_engagement
    return render_template('statistic.html', students=students, user=user)


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))

    admin = Admin()

    if request.method == 'POST':
        if request.form.get('delete'):
            username = request.form.get('username')
            admin.delete_user(username)
            flash('User profile deleted successfully!')
        elif request.form.get('update'):
            username = request.form.get('username')
            attendance = request.form.get('attendance')
            sdlc_quiz_pct = request.form.get('sdlc_quiz_pct')
            applied_maths_quiz_pct = request.form.get('applied_maths_quiz_pct')
            iot_quiz_pct = request.form.get('iot_quiz_pct')
            ssd_quiz_pct = request.form.get('ssd_quiz_pct')
            sdlc_tutor_score = request.form.get('sdlc_tutor_score')
            applied_maths_tutor_score = request.form.get('applied_maths_tutor_score')
            ssd_tutor_score = request.form.get('ssd_tutor_score')
            iot_tutor_score = request.form.get('iot_tutor_score')
            flash(admin.update_statistics(username, attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct,
                                          iot_quiz_pct, sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score,
                                          iot_tutor_score))

    return render_template('admin.html')



if __name__ == "__main__":
    app.run(debug=True)