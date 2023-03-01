import sqlite3


class Users:

    def __init__(self, username,password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def get_students():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_type='student'")
        users = []
        for row in cursor.fetchall():
            user = Users(row[0], row[1], row[2])
            users.append(user)
        conn.close()
        return users