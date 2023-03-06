import sqlite3
from flask import session
class Users:
    def __init__(self, username, password, role, degree, name,year):
        self.permission = None
        self.username = username
        self.password = password
        self.role = role
        self.degree = degree
        self.name = name
        self.year=year
        self.attendance = None
        self.quiz_submissions = None
        self.tutor_engagement = None
    @staticmethod
    def get_user():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = []
        for row in cursor.fetchall():
            user = Users(row[0], row[1], row[2],row[3],row[4],row[5])
            users.append(user)
        conn.close()
        return users

    @staticmethod
    def get_student_by_username(username):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if row is None:
            return None
        user = Users(row[0], row[1], row[2], row[3], row[4],row[5])
        conn.close()
        return user

    @staticmethod
    def get_user_type(username):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        query = f"SELECT user_type FROM users WHERE username = '{username}'"
        cur.execute(query)
        result = cur.fetchone()
        con.close()

        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def search_users(search_term):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username LIKE ? OR name LIKE ?",
                       (f"%{search_term}%", f"%{search_term}%"))
        users = []
        for row in cursor.fetchall():
            user = Users(row[0], row[1], row[2], row[3], row[4],row[5])
            users.append(user)
        conn.close()
        return users


