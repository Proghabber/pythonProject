import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as massege
import json
import sqlite3
import threading
import time
import db_class



class Win(tkinter.Tk):
        def __init__(self,):
            super().__init__()
            self.info_json="base_data/info.json"
            self.name ="name_competer"
            self.password=""
            self.path_to_db ="base_data/sik.db"
            self.list_wiget = []#self.tab1,
            self.admin = "user"
            self.user_db=db_class.Users(db_class.cursor)
            self.enter_accept=False

            #боксы
            #первая вкладка
            self.tabControl = ttk.Notebook(self)
            self.tab1 = ttk.Frame(self.tabControl)
            self.frame_info = Frame(self.tab1, height=20)
            self.frame_text = Frame(self.tab1)
            self.frame_sent = Frame(self.tab1, height=20)


            self.data_frame=Frame(self.frame_info)
            self.date_label = Label(self.data_frame, text="Дата сегодня - ")
            self.date_now = Label(self.data_frame, text=self.return_date())
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
            self.frame_info.pack(anchor=W,expand=1,fill=BOTH,)
            self.frame_sent.pack(anchor=W, pady=2, expand=0, fill=X)
            self.data_frame.pack(side=LEFT,expand=1,fill=BOTH )
            self.date_label.pack(side=TOP, ipadx=10)
            self.date_now.pack(side=TOP, ipadx=10)
            self.frame_text.pack(expand=1, fill=BOTH, side=LEFT,ipady=90 )
            self.text_enter.pack(in_=self.frame_text, anchor=NW, expand=1, fill=BOTH, side=LEFT, )
            self.text_enter_themm.pack(anchor=N, expand=1, fill=X, side=BOTTOM,)
            self.batton_send_info.pack(side=LEFT)
            self.scrol_text.pack(in_=self.frame_text, anchor=NE, fill=Y, side=RIGHT,)



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

        def show_pass(self,list):
            """
            делает пароль видимым
            :return:
            """
            for i in list:
                if i['show']=="*":
                    i.config(show="")
                else:
                    i.config(show="*")

        def compare_pass(self,list):
            """
            проверяет пароли на длинну и совпадение
            :param list:  список паролей
            :return:
            """
            print(list)
            if len(list[0].get())<8 or len(list[1].get())<8:
                list[0].delete(0,END)
                list[1].delete(0, END)
                massege.showerror("Внимание","Длинна пароля не должна быть меноше 8 символов")
            else:
                if list[0].get()!=list[1].get():
                    list[0].delete(0, END)
                    list[1].delete(0, END)
                    massege.showerror("Внимание","Пароли не совпадают")
                else:
                    print("good,go to...", list[2].get(), list[1].get())
                    login=list[2].get()
                    password=list[1].get()
                    list[0].delete(0, END)
                    list[1].delete(0, END)
                    self.name=list[2].get()
                    try:
                        self.user_db.write_db(login, password)
                        massege.showerror("Успех",f"{self.name} регистрация успешна")
                        self.enter_accept=True
                        self.name=self.name
                        self.enter_access()
                    except:

                        massege.showerror("Ошибка", f"{self.name} регистрация ощибка")

                    #self.know_name()




        def meet_user(self,login,password):
            """

            """
            login_new=login.get()
            password_new=password.get()



            try:
                if not self.user_db.enter_programm(login_new,password_new):
                    massege.showerror("Ошибка","ошибка")
                    password.delete(0, END)
                else:
                    massege.showerror("Вход", f"{login_new} привет")
                    self.name=login_new
                    self.enter_accept=True
                    self.enter_access()


            except:
                massege.showerror("Ошибка", "Ошибка в базе данных")
                pass

        def enter_access(self):

            self.destry_widget()
            self.list_wiget = []
            frame_name=Frame(self.frame_info)
            label_name=Label(text=f"Пользователь-\n{self.name} ")
            frame_name.pack(side=LEFT, expand=1, fill=BOTH, padx=10, pady=2)
            label_name.pack(in_=frame_name,side=LEFT,expand=1, fill=BOTH, padx=10, pady=2)
            self.list_wiget.extend((frame_name,label_name))




        def hi_client(self):
            self.destry_widget()
            self.list_wiget = []
            frame_enter_all = Frame(self.frame_info)
            frame_enter=Frame(frame_enter_all,bg="red")

            hi_client=Label(text="Войдите или зарегистрируйтесь",bg="yellow")
            button_enter=Button(text="Войти",command=lambda: self.enter_programm(),height=1)
            button_reg=Button(text="Регистрация",command=lambda: self.no_name(),height=1)
            frame_enter_all.pack(side=LEFT, expand=1, fill=BOTH, padx=10, pady=2)
            hi_client.pack(in_=frame_enter_all, side=TOP,expand=1, fill=BOTH, padx=10, pady=2)
            frame_enter.pack(side=TOP, expand=1, fill=BOTH, padx=10, pady=2)

            button_reg.pack(in_=frame_enter,anchor=CENTER)
            button_enter.pack(in_=frame_enter,anchor=CENTER)

            self.list_wiget.extend((frame_enter_all,frame_enter,hi_client,button_enter,button_reg))



        def enter_programm(self):
            self.destry_widget()
            self.list_wiget = []
            klient = Label(text="Имя клиента", anchor=W)
            text_klient = Entry(width=10, bg="white", fg="black")
            klient_name = Button(text="Войти",command=lambda :self.meet_user(text_klient,text_klient_pass_l),height=1, )
            klient_pass_l = Label(text="Пароль", anchor=W)
            text_klient_pass_l = Entry(width=10, show="*", bg="white", fg="black")
            pass_pass=Label(width=1,height=1, anchor=W)

            frame_lable = Frame(self.frame_info)
            frame_text = Frame(self.frame_info)
            button_exit = Button(text="Назад",command=lambda: self.hi_client(),height=1, )
            button_pass_show = Button(text="Показать", command=lambda: self.show_pass((text_klient_pass_l,)), height=1, )
            frame_lable.pack(side=LEFT, expand=1, fill=BOTH, padx=10, pady=2)
            frame_text.pack(side=LEFT, expand=1, fill=BOTH, padx=10, pady=2)
            # 1
            klient.pack(in_=frame_lable, side=TOP, expand=1, fill=BOTH, padx=10, pady=1)
            klient_pass_l.pack(in_=frame_lable, side=TOP, expand=1, fill=BOTH, padx=10, pady=1)
            klient_name.pack(in_=frame_lable, side=TOP, expand=1, fill=X, padx=10, pady=1)
            button_exit.pack(in_=frame_lable, side=TOP, expand=1, fill=X, anchor=NW, padx=10, pady=2)

            # 2
            text_klient.pack(in_=frame_text, side=TOP, expand=1, fill=BOTH, anchor=NW, padx=10, pady=2)
            text_klient_pass_l.pack(in_=frame_text, side=TOP, expand=1, fill=BOTH, anchor=NW, padx=10, pady=2)
            button_pass_show.pack(in_=frame_text, side=TOP, expand=1, fill=X, anchor=NW, padx=10, pady=2)
            pass_pass.pack(in_=frame_text, side=TOP, expand=1, fill=BOTH, padx=10, pady=1)
            self.list_wiget.extend(( frame_lable, frame_text, klient,
                                    text_klient, klient_name, klient_pass_l,
                                    button_exit ,button_pass_show))




        def no_name(self, ):
            """
            если не авторизирован, то создает виджеты для получения имени и пароля
            :return:
            """
            self.destry_widget()
            self.list_wiget = []
            print(self.list_wiget)
            klient = Label( text="Имя клиента",anchor=W)
            text_klient = Entry(width=30,  bg="white", fg="black")
            klient_name = Button(text="Регистрация",height=1, command=lambda: self.compare_pass((text_klient_pass_l,
                                                                                         text_klient_pass_rep_l,text_klient)))
            klient_pass_l = Label( text="Пароль",anchor=W)
            text_klient_pass_l=Entry(width=30 , show="*", bg="white", fg="black")
            klient_pass_rep_l = Label( text="Пароль повтор",anchor=W)
            text_klient_pass_rep_l=Entry(width=30, show="*", bg="white", fg="black")
            button_pass = Button(text="Показать", height=1, command=lambda: self.show_pass((text_klient_pass_l,
                                                                                            text_klient_pass_rep_l)))
            button_back_of=Button(text="Назад",command=lambda:self.hi_client(),height=1)

            frame_bottom = Frame(self.frame_info)
            frame_lable=Frame(frame_bottom)
            frame_text=Frame(frame_bottom)
            frame_back_of=Frame(self.frame_info)

            frame_bottom.pack(side=TOP,expand=1,fill=X,  padx=10,pady=2)
            frame_lable.pack(side=LEFT,expand=1,fill=BOTH,   padx=10,pady=2)
            frame_text.pack(side=LEFT,expand=1,fill=BOTH,  padx=10,pady=2)
            frame_back_of.pack(side=TOP,expand=1,fill=BOTH,  padx=10,pady=2)
            #1
            klient.pack(in_=frame_lable,side=TOP,expand=1,fill=BOTH,  padx=10,pady=1)
            klient_pass_l.pack(in_=frame_lable,side=TOP,expand=1,fill=BOTH, padx=10,pady=1)
            klient_pass_rep_l.pack(in_=frame_lable,side=TOP,expand=1,fill=BOTH, padx=10,pady=1)
            klient_name.pack(in_=frame_lable,side=TOP,expand=1,fill=BOTH, padx=10,pady=1)
            #2
            text_klient.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            text_klient_pass_l.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            text_klient_pass_rep_l.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            button_pass.pack(in_=frame_text, side=TOP,expand=1,fill=X, anchor=NW, padx=10,pady=2)
            button_back_of.pack(in_=frame_back_of, side=TOP,expand=1,fill=X, anchor=NW, padx=10,pady=2)
            self.list_wiget.extend((button_back_of,frame_back_of,frame_bottom,frame_lable,frame_text,klient,text_klient,klient_name,klient_pass_l,
                                    klient_pass_rep_l,button_pass,text_klient_pass_l,text_klient_pass_rep_l))


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

        def destry_widget(self, ):
            """

            """
            for i in self.list_wiget:
                i.destroy()


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
                cursor.execute("""
                """)
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
            self.list_wiget=[]
            heighre_ = len(self.list_button) * 26
            mane_frame=Frame(self.frame_text_oders,)
            convas = Canvas(mane_frame,bg="gray")
            fremer = Frame(convas, width=0)
            skroll = Scrollbar(convas)
            frame_sarch=Frame(self.frame_text_oders, )
            days = list(range(32))
            months=list(range(13))
            years=list(range(2021,2099))
            sarch_button=Button(text="Sarch")
            fremer.pack(side=RIGHT, fill=BOTH, expand=1)
            convas.create_window((0, 0), window=fremer, width=0, height=heighre_, anchor=N + W)
            self.wiwets.extend([convas, skroll, fremer])
            for i in self.list_button:
                i.pack(in_=fremer, side=TOP, fill=BOTH, expand=1,)
                self.wiwets.append(i)
            skroll.config(command=convas.yview)
            skroll.pack(side=RIGHT, fill=Y, )
            convas.config(yscrollcommand=skroll.set, scrollregion=(0, 0, 0, heighre_), )
            convas.pack(side=LEFT, fill=BOTH, expand=1)
            sarch_button.grid(in_=frame_sarch,row=1,column=4)
            row=0
            column=1
            for i in self.create_wigets("Combobox",6,(days,days,months,months,years,years)):
                if column==3:
                    row+=1
                    column = 1
                i.grid(in_=frame_sarch,row=row,column=column,)
                self.wiwets.append(i)
                column+=1
            row = 0
            column = 0
            for i in  self.create_wigets("lable",6,("from days","from months","from years","to days"," to months",
                                                    "to years")):
                if row==3:
                    row=0
                    column = 3
                i.grid(in_=frame_sarch,row=row,column=column,)
                self.wiwets.append(i)
                row+=1

            frame_sarch.pack()
            mane_frame.pack(side=LEFT, fill=BOTH, expand=1)
            self.wiwets.extend((sarch_button,skroll,fremer,frame_sarch,mane_frame))

        def del_wiget(self):
            """
            отчищает список виджетов
            :return:
            """
            for i in self.wiwets:
                i.pack_forget()
                i.grid_forget()

        def create_wigets(self,types,amount,args):
            return_wigets=[]
            count = 0
            if types=="Combobox":
                for i in range(amount):
                    return_wigets.append(ttk.Combobox(values=args[count]))
                    count+=1
            if types=="lable":
                for i in range(amount):
                    return_wigets.append(Label(text=args[count]))
                    count+=1
            return return_wigets

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
winner.user_db.create_table()
winner.hi_client()
cot=threading.Thread(target=winner.call_of_admin,daemon = True)
cot.start()
winner.mainloop()
