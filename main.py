from flask import Flask, render_template, request, redirect, url_for, flash, session,g
import sqlite3
from users import Users
from mystat import Statistic
from admin import Admin

app = Flask(__name__)
app.secret_key = 'secret'
from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


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
@login_required
def landing():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    user = Users.get_user_type(username)
    return render_template('landing.html', user=user)


@app.route('/statistic')
@app.route('/statistic/<username>')
@login_required
def statistic(username=None):
    if username is None:
        if 'username' not in session:
            return redirect(url_for('login'))
        username = session['username']
    students = Users.get_user()
    user_type=Users.get_user_type(username)
    attendance, quiz_submissions, tutor_engagement = Statistic.get_statistic(username)
    user = Users(username, None, 'student', None, None)
    user.attendance = attendance
    user.quiz_submissions = quiz_submissions
    user.tutor_engagement = tutor_engagement
    return render_template('statistic.html', students=students, user=user,user_type=user_type)





@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/admin', methods=['POST', 'GET'])
@login_required
def admin():
    if 'username' not in session:
        return redirect(url_for('login'))
    admin = Admin()
    if request.method == 'POST':
        if request.form.get('add_user'):
            username = request.form.get('username')
            password = request.form.get('password')
            user_type = request.form.get('user_type')
            degree = request.form.get('degree')
            name = request.form.get('name')
            admin.add_user(username, password,user_type,degree,name)
            flash('User added successfully!')
        elif request.form.get('delete_user'):
            username = request.form.get('username')
            admin.delete_user(username)
            flash('User profile deleted successfully!')
        elif request.form.get('delete'):
            username = request.form.get('username')
            admin.delete_user(username)
            flash('User profile and statisitic deleted successfully!')
        elif request.form.get('update_statistics'):
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
            flash(admin.update_statistics(username,attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct, iot_quiz_pct,
                                       sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score, iot_tutor_score))
        elif request.form.get('add_statistics'):
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
            flash(admin.add_statistics(username,attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct, iot_quiz_pct,
                                       sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score, iot_tutor_score))

    return render_template('admin.html')

@app.route('/permission', methods=['GET', 'POST'])
@login_required
def permission():
    if 'username' not in session:
        return redirect(url_for('login'))

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    if request.method == 'POST':
        for username, user_type in request.form.items():
            query = f"UPDATE users SET user_type = '{user_type}' WHERE username = '{username}'"
            cur.execute(query)
        con.commit()
        flash('User types updated successfully!')

    query = "SELECT username, user_type FROM users"
    cur.execute(query)
    users = cur.fetchall()

    return render_template('permission.html', users=users)

@app.route('/account')
@app.route('/account/<username>')
@login_required
def account(username=None):
    if username is None:
        if 'username' not in session:
            return redirect(url_for('login'))
        username = session['username']
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    query = "SELECT * FROM users"
    cur.execute(query)
    users = cur.fetchall()
    query = f"SELECT * FROM users WHERE username ='"+username+"'"
    cur.execute(query)
    user = cur.fetchone()

    return render_template('account.html', users=users, user=user)


if __name__ == "__main__":
    app.run(debug=True)