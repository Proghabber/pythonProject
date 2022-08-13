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
                password VARCHAR(30) NOT NULL
            );  
            """
        )

    def write_db(self,login,password):
        self.cursor.execute(
            """
            INSERT INTO users(login,password)
            VALUES(?,?)
            """,
            (login,password)
        )
        self.cursor.execute(
            "commit;"
        )
    def enter_programm(self,login,password):
        self.cursor.execute(
            """
            SELECT login,password FROM users WHERE login=? AND password=?
            """,(login,password)

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
    def return_info(self,login):
        self.cursor.execute(
            """
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ?
            """,(login,)

        )
        return self.cursor.fetchall()

    def return_info_dd(self,login,date_last,date_next):
        date_last=[2021,10,21]
        date_next=[2022,10,22]
        #next=
        login="user"

        self.cursor.execute(
            """
            SELECT o.title,o.text, o.status, o.date_created, o.date_accept, o.date_complete, o.who_maked, o.login
            FROM orders AS o 
            JOIN users AS u ON o.login = u.login
            WHERE o.login = ? AND o.date_created BETWEEN '2022-07-30' AND '2022-08-31'
            """, ([login])

        )
        return self.cursor.fetchall()


    def write_order(self,title,text,login):
        self.cursor.execute(
            """
                INSERT INTO orders(title,text,login)
                VALUES(?,?,?)
            """,
            (title,text,login)
        )
        self.cursor.execute("commit;")


