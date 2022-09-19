import sqlite3
import datetime
# with sqlite3.connect("bd.db") as db:
#     cursor=db.cursor()
#     query=""" CREATE TABLE IF NOT EXISTS client(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR
#     )"""
#     cursor.execute(query)
#
# with sqlite3.connect("bd.db") as db:
#     cursor=db.cursor()
#     one="""INSERT INTO client(name) VALUES("RIO")"""
#     cursor.execute(one)
#
conect=sqlite3.connect("base_data/work.db")
cursor=conect.cursor()

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
    def return_who_accept(self,id,):
        select_info=""" SELECT who_maked FROM orders  WHERE id=?"""
        list_info = (id,)
        self.cursor.execute(select_info, list_info)
        return self.cursor.fetchone()

    def return_info(self,login):
        self.cursor.execute(
            """
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login,o.id
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ?
            """,(login,)

        )
        return self.cursor.fetchall()

    def return_info_dd(self,login,date_last,date_next):
        self.cursor.execute(
            """
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ? AND o.date_created BETWEEN ? AND ?
            """, ([login,date_last,date_next])

        )
        return self.cursor.fetchall()

    def return_info_ddw(self,login,date_last,date_next,word):
        self.cursor.execute(
            f"""
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ? AND o.title LIKE '%{word}%' OR o.text LIKE '%{word}%'
            AND o.date_created BETWEEN ? AND ? 
            
            
            """, ([login,date_last,date_next])

        )
        return self.cursor.fetchall()

    def return_info_d(self, login, date_last,):
        self.cursor.execute(
            f"""
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ? AND o.date_created LIKE '%{date_last}%'
            """, ([login])

        )
        return self.cursor.fetchall()

    def return_info_w(self, login,word):
        self.cursor.execute(
            f"""
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ? AND o.title LIKE '%{word}%' OR o.text LIKE '%{word}%'
             


            """, ([login])

        )
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

    def update_order(self,process,id_order,who_accept):
        if process=="accept":
            apdate_info = """UPDATE orders SET status = ?, who_maked = ?, date_accept = datetime('now', 'localtime') WHERE id = ?"""
            column_info = ("Взято на контроль",who_accept, id_order,)
            self.cursor.execute( apdate_info, column_info)
            self.cursor.execute("commit;")
        elif process=="complete":
            pass




