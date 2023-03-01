import sqlite3
class Statistic:
    def __init__(self, username, attendance, software_dev, applied_maths, smart_solutions, iot, eng_score_software,
                 eng_score_maths, eng_score_solutions, eng_score_iot):
        self.username = username
        self.attendance = attendance
        self.software_dev = software_dev
        self.applied_maths = applied_maths
        self.smart_solutions = smart_solutions
        self.iot = iot
        self.eng_score_software = eng_score_software
        self.eng_score_maths = eng_score_maths
        self.eng_score_solutions = eng_score_solutions
        self.eng_score_iot = eng_score_iot

    def get_statistic(username):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM statistics WHERE username=?", (username,))
        row = cursor.fetchone()
        attendance = row[1]
        quiz_submissions = {
            'Software Development and Lifecycle': row[2],
            'Applied Maths': row[3],
            'Smart Solutions Development': row[4],
            'Internet of Things': row[5]
        }
        tutor_engagement = {
            'Software Development and Lifecycle': row[6],
            'Applied Maths': row[7],
            'Smart Solutions Development': row[8],
            'Internet of Things': row[9]
        }
        conn.close()
        return attendance, quiz_submissions, tutor_engagement
