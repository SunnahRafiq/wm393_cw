import sqlite3


class User:

    def __init__(self, username, user_type):
        self.username = username
        self.user_type = user_type

def get_students():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, user_type FROM users WHERE user_type = 'student'")
    rows = cursor.fetchall()
    users = [User(row[0], row[1]) for row in rows]
    conn.close()
    return users