import sqlite3
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
            status VARCHAR(255) NOT NULL,
            date_created DECIMAL(100,2) NOT NUL,
            date_accept DECIMAL(100,2) NOT NUL,
            comment TEXT,
            login TEXT NOT NULL,
            FOREIGN KEY(login) REFERENCES users(login)
            )
            """
        )