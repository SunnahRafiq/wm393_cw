import sqlite3


class Users:
    def __init__(self, username, password, role, degree, name):
        self.permission = None
        self.username = username
        self.password = password
        self.role = role
        self.degree = degree
        self.name = name
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
            user = Users(row[0], row[1], row[2],row[3],row[4])
            users.append(user)
        conn.close()
        return users

    def get_student_by_username(username):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if row is None:
            return None
        user = Users(row[0], row[1], row[2], row[3], row[4])
        conn.close()
        return user

    def is_admin(self):
        return self.role == 'admin'
