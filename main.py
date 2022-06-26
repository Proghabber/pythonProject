import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as massege
import json
import sqlite3
import threading
import time



class Win(tkinter.Tk):
        def __init__(self,):
            super().__init__()
            self.info_json="base_data/info.json"
            self.name ="name_competer"
            self.path_to_db ="base_data/sik.db"
            self.list_wiget = []#self.tab1,
            self.admin = "user"

            #боксы
            #первая вкладка
            self.tabControl = ttk.Notebook(self)
            self.tab1 = ttk.Frame(self.tabControl)
            self.frame_info = Frame(self.tab1, height=20)
            self.frame_text = Frame(self.tab1)
            self.frame_sent = Frame(self.tab1, height=20)
            self.klient = Label(self.frame_info, text="Имя клиента - ")
            self.date_label = Label(self.frame_info, text="Дата сегодня - ")
            self.date_now = Label(self.frame_info, text=self.return_date())
            self.text_enter = Text(self.frame_text, width=0, )
            self.text_enter_themm = Text(self.frame_sent, height=1)
            self.scrol_text = Scrollbar(self.tab1, command=self.text_enter.yview)
            self.batton_send_info = Button(self.frame_sent, text="Отправить",command=lambda  :self.write_table())
            #вторая вкладка
            self.tab2 = ttk.Frame(self.tabControl)
            self.frame_tab2 = Frame(self.tab2)
            self.frame_text_oders = Frame(self.frame_tab2, )

            self.list_button_info = []
            self.list_button = []
            self.wiwets = []



        def set_parametrs(self):
            self.title("Программа оформления заявок")
            self.geometry(f"{660}x{500}")
            self.tabControl.add(self.tab1, text='Составить заявку')
            self.text_enter.insert(INSERT, "Cообщение")
            self.text_enter_themm.insert(INSERT, "Тема", )
            self.text_enter.config(yscrollcommand=self.scrol_text.set)
            self.tabControl.add(self.tab2, text='Посмотреть заявки')
            self.tabControl.bind('<Button-1>', lambda e: self.click_to_notebook())

        def pack_widgets(self):
            self.frame_info.pack(anchor=W)
            self.frame_sent.pack(anchor=W, pady=2, expand=0, fill=X)
            self.date_label.pack(side=LEFT, ipadx=10)
            self.date_now.pack(side=LEFT, ipadx=10)
            self.frame_text.pack(expand=1, fill=BOTH, side=LEFT, )
            self.text_enter.pack(in_=self.frame_text, anchor=NW, expand=1, fill=BOTH, side=LEFT, )
            self.text_enter_themm.pack(anchor=N, expand=1, fill=X, side=BOTTOM)
            self.batton_send_info.pack(side=LEFT)
            self.scrol_text.pack(in_=self.frame_text, anchor=NE, fill=Y, side=RIGHT)
            self.klient.pack(side=LEFT, ipadx=10)
            self.tab1.place()
            self.tabControl.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.frame_text_oders.pack(anchor=NW, expand=1, fill=BOTH, )
            self.frame_tab2.place(relx=0, rely=0, relwidth=1, relheight=1)

            self.tab2.place()
            self.tabControl.place(relx=0, rely=0, relwidth=1, relheight=1)

        def kalendwr(self,a: list[int]) -> list[str]:
            """получает список интов и преобразует в список строк и если получился один знак ,то добавляет перед ним 0"""
            b = []
            for i in a:
                i = str(i)

                if len(i) < 2:
                    i = "0" + i
                b.append(i)
            return b

        def return_date(self):
            """
            получает дату и форматирует ее
            :return:
            """
            date = datetime.datetime.today()
            date_chenge = self.kalendwr([date.day, date.month, date.year])
            return date_chenge

        def meet_user(self):
            """
                    опредиляет сохранено имя в файле, если да то дает лабел с именем на табло, иначе запускает скрипт
                    получения имени
            """
            try:
                with open(self.info_json, "r") as read_file:
                    info1 = json.load(read_file)
                    self.name = info1["name_competer"]
                    self.path = info1["path"]
                    text = Label(text=self.name)
                    text.pack(in_=self.frame_info, side=LEFT, ipadx=10)

            except:
                self.no_name()


        def no_name(self, ):
            """
            если имени нет, то создает виджеты для получения имени
            :return:
            """

            self.list_wiget = []
            text_info = Text(width=10, height=1, bg="white", fg="black")
            klient_name = Button(text="Установить", command=lambda: self.know_name())
            text_info.pack(in_=self.frame_info, side=LEFT, ipadx=10)
            klient_name.pack(in_=self.frame_info, side=LEFT, ipadx=10)
            self.list_wiget.append(text_info)
            self.list_wiget.append(klient_name)

        def runame(self, ):
            """
            записывает полученое имя в json файл
            :return:
            """
            info = {"name_competer": self.name, "path": self.path_to_db}
            try:
                with open(self.info_json, "w") as write_file:
                    json.dump(info, write_file, ensure_ascii=False)
            except:
                pass

        def know_name(self, ):
            """
            когда имя введино(нажата кнопка), получает значение поля и удаляет старые виджеты
            :return:
            """
            for i in self.list_wiget:
                if i.winfo_class() == "Text":
                    self.name = i.get(1.0, END)[0:-1]
                i.destroy()
            text = Label(text=self.name)
            text.pack(in_=self.frame_info, side=LEFT, ipadx=10)
            self.runame()

        def get_name(self):
            return self.name
#функции sql
        def create_bd(self):
            """
            создает базу данных
            :return:
            """
            with sqlite3.connect(self.path_to_db) as content:
                cursor = content.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS "self.name"(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client VARCHAR,
                topic VARCHAR,
                text TEXT,
                status TEXT
                )""")

        def print_table(self):
            """
            возвращает список из базы данных
            :return:
            """
            with sqlite3.connect(self.path_to_db) as content:
                cursor = content.cursor()
                cursor.execute("SELECT *FROM 'self.name'")
                return cursor.fetchall()

        def clear_inter(self, list):
            """
            форматирует список удаляя "\n" где надо
            :param list:
            :return:
            """
            index = 0
            bow_new = []
            for box in list[0]:
                word = ''
                if index != 2:
                    for lit in box:
                        if lit != "\n":
                            word = word + lit
                else:
                    word = box
                bow_new.append(word)
                index += 1
            list_new = [tuple(bow_new)]

            return list_new

        def write_table(self,):
            """
            записывает данные в бд
            :return:
            """
            data=self.collect_info()
            data = self.clear_inter(data)
            with sqlite3.connect(self.path_to_db) as content:
                cursor = content.cursor()
                cursor.execute("SELECT *FROM 'self.name'")
                if data[0][1] != "трипер":
                    self.admin = "user"
                    if data[0][0] != "":
                        cursor.executemany("INSERT INTO 'self.name'(client, topic, text, status) VALUES(?,?,?,?)", data)
                        massege.showerror("Отправка", "Заявка отправлена")

                    else:
                        massege.showerror("Oшибка", "Авторизируйтесь чтобы отправить заявку")
                else:
                    self.admin = "admin"
                    massege.showerror("Внимание", "Вы получили права админа")





        def update_info(self,data):
            """
            обнавляет параметр статус в бд
            :param data:
            :return:
            """
            with sqlite3.connect(self.path) as content:
                cursos = content.cursor()
                cursos.execute("SELECT id  FROM 'self.name'")
                cursos.execute("UPDATE  'self.name'  SET status = 'Исполнено' WHERE id = (?)", [data[0]])

        # вернуть функции cathe_sql  call_of_admin
#функции для вкладки "составить заявку"
        def collect_info(self):
            """
            собирает данные по заявке для отправки в бд
            :return:
            """
            name=self.name
            themm=self.text_enter_themm.get(1.0, END)
            text=self.text_enter_themm.get(1.0, END)
            status="Актуально"
            return ([(name,themm,text,status)])
#функции для вкладки "показать заявки"

        def count_button(self,  ):
            """
            Из полученных данных формирует информацию для будующих кнопок.
            :param data: данные из sql таблици
            :return:
            """
            data=self.print_table()

            self.list_button_info = []
            name_computer = ""
            if self.admin == "user":
                name_computer = "user"
            else:
                name_computer = "admin"

            for i in data:
                zip = []
                for biter in i:
                    word = ""
                    for liter in str(biter):
                        if liter != "\n":
                            word = word + liter
                    if i[1] == self.name or name_computer == "admin":
                        zip.append(word)
                if zip:
                    self.list_button_info.append(zip)



        def create_button(self, ):
            """
            Перебирает инфу для кнопок и запускает функцию создания кнопки
            :return:
            """
            self.list_button = []
            for i in self.list_button_info:
                self.create_but(i)

        def create_but(self,text):
            """
            создают кнопку и функцию к ней прекрепляет, ложет ее в список
            :param text:
            :return:
            """

            if len(text[3]) > 10:
                len_mass = 10
            else:
                len_mass = len(text[3])
            but = Button(text=f"{text[0]} {text[1]} {text[2]}-{text[3][0:len_mass]}",
                         command=lambda: self.put_text(text))
            self.list_button.append(but)

        def put_button(self, ):
            """
            расставляет кнопки на экране
            :return:
            """
            self.del_wiget()
            heighre_ = len(self.list_button) * 26
            convas = Canvas(self.frame_text_oders, height=heighre_, width=0)
            fremer = Frame(convas, width=0)
            skroll = Scrollbar(convas)
            fremer.pack(side=RIGHT, fill=BOTH, expand=1)
            convas.create_window((0, 0), window=fremer, width=0, height=heighre_, anchor=N + W)
            self.wiwets.extend([convas, skroll, fremer])
            for i in self.list_button:
                i.pack(in_=fremer, side=TOP, fill=BOTH, expand=1)
            skroll.config(command=convas.yview)
            skroll.pack(side=RIGHT, fill=Y, )
            convas.config(yscrollcommand=skroll.set, scrollregion=(0, 0, 0, heighre_), )
            convas.pack(side=LEFT, fill=BOTH, expand=1)

        def del_wiget(self):
            """
            отчищает список виджетов
            :return:
            """
            for i in self.wiwets:
                i.pack_forget()

        def put_text(self, text):
            """
            формерует и размещает текст и текстовое поле на экране
            :param text:
            :return:
            """
            self.del_wiget()
            frame_but = Frame(self.frame_text_oders)
            but_back = Button(frame_but, text="Назад", command=lambda: self.put_button())
            chec_statys = Button(frame_but, text="Выполнено", command=lambda: self.update_status(text))
            tex_teria = Text(self.frame_text_oders, width=0)
            tex_teria.insert(1.0, f"Заявитель-{text[1]}\nТема-{text[2]}\nCтатус-{text[4]}\nCообщение:\n{text[3]}")
            skrol_text = Scrollbar(self.frame_text_oders, command=tex_teria.yview)
            tex_teria.config(yscrollcommand=skrol_text.set)
            self.wiwets.extend((frame_but, but_back, chec_statys, tex_teria, skrol_text))
            but_back.pack(side=LEFT)
            chec_statys.pack(side=RIGHT)
            frame_but.pack(side=TOP)
            tex_teria.pack(side=LEFT, fill=BOTH, expand=1)
            skrol_text.pack(side=RIGHT, fill=Y)

        def update_status(self,data):
            """
            обновляет статус заказа в таблице и для кнопок
            :param data:
            :return:
            """

            self.update_info(data)
            self.create_button()
            data[4] = "Исполнено"
            self.put_text(data)
            massege.showerror("Изменение", "Заявка отмечена как 'выполенно'")

        def click_to_notebook(self):
            self.count_button()
            self.create_button()
            self.put_button()


        def call_of_admin(self, ):
            """
            если режим админа запужен иледит за бд и выдает сообщение  при ее изменении
            :return:
            """
            len_sql=len(self.print_table())
            while True:
                time.sleep(2)
                if self.admin=="admin" and len(self.print_table())>len_sql:
                    len_sql=len(self.print_table())
                    list_info=self.print_table()[0]
                    info=[list_info[1],list_info[2]]
                    massege.showerror("Внимание",f"Новая заявка:\n заявитель-{info[0]} тема-{info[1]}")







winner=Win()
winner.set_parametrs()
winner.pack_widgets()
winner.meet_user()
cot=threading.Thread(target=winner.call_of_admin,daemon = True)
cot.start()
winner.mainloop()
