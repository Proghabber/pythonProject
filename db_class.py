import sqlite3

def path_(path):
    conect=sqlite3.connect(path)
    cursor=conect.cursor()
    return cursor

class Users():
    def __init__(self,cursor):
        self.cursor=cursor

    def create_table(self,):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login VARCHAR(30) NOT NULL UNIQUE,
                user_type VARCHAR(30) NOT NULL,
                password VARCHAR(30) NOT NULL
            );  
            """
        )

    def write_db(self,login,password,klient_type):
        self.cursor.execute(
            """
            INSERT INTO users(login,password,user_type)
            VALUES(?,?,?)
            """,
            (login,password,klient_type)
        )
        self.cursor.execute(
            "commit;"
        )
    def enter_programm(self,login,password):
        self.cursor.execute(
            """
            SELECT login,password,user_type FROM users WHERE login=? AND password=?
            """,(login,password)

        )

        return self.cursor.fetchall()

    def return_all_users(self):
        self.cursor.execute(
            """
            select login FROM users"""
        )
        return self.cursor.fetchall()




class Orders():
    def __init__(self,cursor):
        self.cursor=cursor


    def create_table(self,):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            text TEXT NOT NULL,
            status VARCHAR(255)  NOT NULL DEFAULT "Активно",
            date_created DATETIME DEFAULT (datetime('now', 'localtime')),
            date_accept DATETIME,
            date_complete DATETIME,
            who_maked VARCHAR(255),
            comment TEXT,
            login TEXT NOT NULL,
            FOREIGN KEY(login) REFERENCES users(login)
            );
            """
        )

    def create_reqest(self,whats_reqest, login,date_last,date_next,word,key):
        parts_reqest=[f"""AND o.date_created BETWEEN ? and ?""",f"""AND o.date_created LIKE "%{date_last}%" """,f"""AND status = ?""",f"""AND (o.title LIKE "%{word}%" OR o.text LIKE "%{word}%")"""]
        base_reqest=f"""
            SELECT o.title, o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login,o.id, o.comment
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ?"""
        elements=[login]
        #date_last="2022-10-09 23:36:05"
        if key=="*":
            parts_reqest[2]=""
        if whats_reqest=="all":
            base_reqest=base_reqest+parts_reqest[0]+parts_reqest[2]+parts_reqest[3]
            elements.extend([date_last,date_next,key,])
        elif whats_reqest=="period":
            base_reqest=base_reqest+parts_reqest[0]+parts_reqest[2]
            elements.extend([date_last, date_next,key,])
        elif whats_reqest=="day_word":
            base_reqest=base_reqest+parts_reqest[1]+parts_reqest[3]+parts_reqest[2]
            elements.extend([ date_next,key,])
        elif whats_reqest=="day":
            base_reqest=base_reqest+parts_reqest[1]+parts_reqest[2]
            elements.extend([key])
        elif whats_reqest=="word":
            base_reqest=base_reqest+parts_reqest[3]+parts_reqest[2]
            elements.extend([key])
        elif whats_reqest=="list":
            base_reqest = base_reqest +parts_reqest[2]
            elements.extend([key])

        elements=[el for el in elements if (el != "*" and el != None)]

        return [base_reqest,elements]



    def return_info_reqest(self,whats_reqest, login,date_last,date_next,word,key):
        reqest=self.create_reqest(whats_reqest,login,date_last,date_next,word,key)

        try:
            self.cursor.execute(reqest[0], reqest[1])
        except:
            pass
        return self.cursor.fetchall()



    def write_order(self,title,text,login):
        self.cursor.execute(
            """
                INSERT INTO orders(title,text,login)
                VALUES(?,?,?)
            """,
            ([title,text,login])
        )
        self.cursor.execute("commit;")

    def update_order(self,process,id_order,who_accept,comemnt):
        apdate_info=None
        column_info=[]
        if process=="accept":
            apdate_info = """UPDATE orders SET status = ?, who_maked = ?, date_accept = datetime('now', 'localtime') WHERE id = ?"""
            column_info = ["Взято на контроль",who_accept, id_order,]
        elif process=="complete":
            apdate_info = """UPDATE orders SET status = ?, date_complete = datetime('now', 'localtime') WHERE id = ?"""
            column_info = ["Выполнено",id_order,]
        elif process=="comment":
            apdate_info = """UPDATE orders SET comment = ? WHERE id = ?"""
            column_info = [comemnt,id_order,]
        self.cursor.execute(apdate_info, column_info)
        self.cursor.execute("commit;")




