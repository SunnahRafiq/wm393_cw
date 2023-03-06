import sqlite3

class Admin:
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()

    def delete_user(self, username):
        self.cur.execute("DELETE FROM users WHERE username=?", (username,))
        self.cur.execute("DELETE FROM statistics WHERE username=?", (username,))
        self.con.commit()



    def update_statistics(self, username, attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct, iot_quiz_pct,
                          sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score, iot_tutor_score):
        if int(attendance) > 100 or int(sdlc_quiz_pct) > 100 or int(applied_maths_quiz_pct) > 100 or int(
                iot_quiz_pct) > 100 or int(ssd_quiz_pct) > 100:
            return 'Attendance or quiz scores cannot be over 100.'
        elif int(sdlc_tutor_score) > 10 or int(applied_maths_tutor_score) > 10 or int(ssd_tutor_score) > 10 or int(
                iot_tutor_score) > 10:
            return 'Tutor scores cannot be over 10.'
        else:
            self.cur.execute("""UPDATE statistics SET
                               sdlc_quiz_pct = ?,
                               sdlc_tutor_score = ?,
                               applied_maths_quiz_pct = ?,
                               applied_maths_tutor_score = ?,
                               ssd_quiz_pct = ?,
                               ssd_tutor_score = ?,
                               iot_quiz_pct = ?,
                               iot_tutor_score = ?,
                               attendance = ?
                               WHERE username = ?""",
                        (sdlc_quiz_pct, sdlc_tutor_score, applied_maths_quiz_pct, applied_maths_tutor_score,
                         ssd_quiz_pct, ssd_tutor_score, iot_quiz_pct, iot_tutor_score, attendance, username))

            # Commit the changes and close the connection
            self.con.commit()
            return 'Statistics updated successfully!'

    def add_user(self, username, password,user_type,degree,name,year):
        self.cur.execute("INSERT INTO users (username, password,user_type,degree,name,year) VALUES (?, ?,?,?,?,?)", (username, password,user_type,degree,name,year))
        self.con.commit()


    def add_statistics(self,username, attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct, iot_quiz_pct,
                       sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score, iot_tutor_score):
        if int(attendance) > 100 or int(sdlc_quiz_pct) > 100 or int(applied_maths_quiz_pct) > 100 or int(
                iot_quiz_pct) > 100 or int(ssd_quiz_pct) > 100:
            return 'Attendance or quiz scores cannot be over 100.'
        elif int(sdlc_tutor_score) > 10 or int(applied_maths_tutor_score) > 10 or int(ssd_tutor_score) > 10 or int(
                iot_tutor_score) > 10:
            return 'Tutor scores cannot be over 10.'
        else:
            self.cur.execute('''INSERT INTO statistics (username,attendance, sdlc_quiz_pct, applied_maths_quiz_pct, ssd_quiz_pct, iot_quiz_pct,
                                       sdlc_tutor_score, applied_maths_tutor_score, ssd_tutor_score, iot_tutor_score)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      ( username,sdlc_quiz_pct, sdlc_tutor_score,
                       applied_maths_quiz_pct, applied_maths_tutor_score,
                       ssd_quiz_pct, ssd_tutor_score,
                       iot_quiz_pct, iot_tutor_score,
                       attendance))

            self.con.commit()
            return 'Statistics added successfully!'