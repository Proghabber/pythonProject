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
import search_class






class Win(tkinter.Tk):
        def __init__(self,):
            super().__init__()
            self.info_json="json/info.json"
            self.name ="name_competer"
            self.pass_=""
            self.password=""
            self.path_to_db = "venv/base_data/work.db"
            self.list_wiget = []#self.tab1,
            self.list_wiget_comment=[]
            self.admin = "user"
            self.user_db=db_class.Users(db_class.path_(self.get_json()["path"]))
            self.oders_db=db_class.Orders(db_class.path_(self.get_json()["path"]))
            self.enter_accept=False
            self.sarch_combobox={}
            self.pass_checked=IntVar()


            #боксы
            #первая вкладка
            self.tabControl = ttk.Notebook()
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
            self.batton_send_info = Button(self.frame_sent, text="Отправить",
                                           command=lambda :self.ask_user("Внимание","Вы хотите отправить сообщение?",
                                                                           self.write_table,[]))
            #вторая вкладка
            #self.pallat=Frame(self)
            self.tab2 = ttk.Frame(self.tabControl,)
            self.frame_tab2 = Frame(self.tab2)
            self.frame_text_oders = Frame(self.frame_tab2, )

            self.list_button_info = []
            self.list_button = []
            self.wiwets = []
            self.exit_programm = Button(self.tabControl,height=1, text="Выход",command=lambda :self.ask_user("Внимание","Вы хотите покинуть программу?",
                                                                           exit,[]))



        def set_parametrs(self):


            self.title("Программа оформления заявок")
            self.geometry(f"{660}x{500}")
            self.tabControl.add(self.tab1, text='Составить заявку')
            self.text_enter.insert(INSERT, "Cообщение")
            self.text_enter_themm.insert(INSERT, "Тема", )
            self.text_enter.config(yscrollcommand=self.scrol_text.set)
            self.tabControl.add(self.tab2, text='Посмотреть заявки')
            self.tabControl.bind('<Button-1>', lambda e: self.put_button("not_creete_button"))


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

            self.tabControl.place(in_=self,relx=0, rely=0, relwidth=1, relheight=1)
            self.frame_text_oders.pack(anchor=NW, expand=1, fill=BOTH, )
            self.frame_tab2.place(relx=0, rely=0, relwidth=1, relheight=1)
            self.tab2.place()
            self.exit_programm.pack(anchor=NE,padx=20, )






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
                    login=list[2].get()
                    password=list[1].get()
                    klient_type=list[3].get()
                    list[0].delete(0, END)
                    list[1].delete(0, END)
                    try:
                        self.user_db.write_db(login,password,klient_type)
                        self.enter_accept=True
                        self.name=login
                        if self.pass_checked.get()==1:
                            self.pass_ = password
                        self.enter_access()
                        massege.showinfo("Успех", f"{self.name} регистрация успешна")
                        self.runame()

                    except:

                        massege.showerror("Ошибка", f"{self.name} регистрация ошибка")



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
                    massege.showinfo("Вход", f"{login_new} привет")
                    self.admin=self.user_db.enter_programm(login_new, password_new)[0][2]
                    self.name=login_new
                    self.enter_accept=True
                    self.enter_access()



            except:
                massege.showerror("Ошибка", "Ошибка в базе данных")
                pass

        def enter_access(self):
            """
            что происходит когда пользователь вошел
            """

            self.del_wiget(self.list_wiget)
            frame_name=Frame(self.frame_info)
            label_name=Label(text=f"Пользователь-\n{self.name} ")
            exit_clien=Button(text="Сменить пользователя",command=lambda :self.ask_user("Внимание","Вы уверены что"
                            " хотите сменить пользователя?",self.hi_client,[]))
            frame_name.pack(side=LEFT, expand=1, fill=BOTH, padx=10, pady=2)
            label_name.pack(in_=frame_name,side=LEFT,expand=1, fill=BOTH, padx=10, pady=2)
            exit_clien.pack(in_=frame_name,side=LEFT,expand=1, fill=BOTH, padx=10, pady=2)
            self.list_wiget.extend((frame_name,label_name,exit_clien))




        def hi_client(self):
            """
            что происходит при запуске программы
            """
            self.del_wiget(self.list_wiget)
            self.list_wiget=[]

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
            """
            выбрана опция войти на экране привецтвия
            """

            self.del_wiget(self.list_wiget)
            self.list_wiget=[]
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
                                    button_exit ,button_pass_show,text_klient_pass_l,pass_pass))




        def no_name(self, ):
            """
            если не авторизирован, то создает виджеты для получения имени и пароля
            :return:
            """
            self.del_wiget(self.list_wiget)
            self.list_wiget=[]
            klient = Label( text="Имя клиента",anchor=W)
            text_klient = Entry(width=30,  bg="white", fg="black")
            klient_name = Button(text="Регистрация",height=1, command=lambda: self.compare_pass((text_klient_pass_l,
                                                                                                text_klient_pass_rep_l,
                                                                                                 text_klient,klient_type)))
            klient_type_l = Label(text="Тип пользователя")
            klient_pass_l = Label( text="Пароль",anchor=W)
            text_klient_pass_l=Entry(width=30 , show="*", bg="white", fg="black")
            klient_pass_rep_l = Label( text="Пароль повтор",anchor=W)

            text_klient_pass_rep_l=Entry(width=30, show="*", bg="white", fg="black")
            klient_type = ttk.Combobox(values=["user", "admin"])
            button_pass = Button(text="Показать", height=1, command=lambda: self.show_pass((text_klient_pass_l,
                                                                                            text_klient_pass_rep_l)))
            button_back_of=Button(text="Назад",command=lambda:self.hi_client(),height=1)
            check_pass=Checkbutton(text="Сохранить пароль",variable=self.pass_checked,)


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
            klient_type_l.pack(in_=frame_lable, side=TOP, expand=1, fill=BOTH, padx=10, pady=1)
            klient_name.pack(in_=frame_lable,side=TOP,expand=1,fill=BOTH, padx=10,pady=1)



            #2
            text_klient.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            text_klient_pass_l.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            text_klient_pass_rep_l.pack(in_=frame_text, side=TOP,expand=1,fill=BOTH, anchor=NW, padx=10,pady=2)
            klient_type.pack(in_=frame_text, side=TOP, expand=1, fill=BOTH, padx=10, pady=1)
            button_pass.pack(in_=frame_text, side=TOP,expand=1,fill=X, anchor=NW, padx=10,pady=2)
            button_back_of.pack(in_=frame_back_of, side=LEFT,expand=1,fill=X, anchor=NW, padx=2,pady=2)
            check_pass.pack(in_=frame_back_of, side=LEFT, padx=2,pady=2)


            self.list_wiget.extend((check_pass,button_back_of,frame_back_of,frame_bottom,frame_lable,frame_text,klient,text_klient,klient_name,klient_pass_l,
                                    klient_pass_rep_l,button_pass,text_klient_pass_l,text_klient_pass_rep_l))


        def runame(self, ):
            """
            записывает полученое имя в json файл
            :return:
            """
            info = {"name_competer": self.name,"pass": self.pass_, "path": self.path_to_db}
            try:
                with open(self.info_json, "w") as write_file:
                    json.dump(info, write_file, ensure_ascii=False)
            except:
                massege.showerror("Ошибка","Ошибка записи json файла")

        def get_json(self):
            """
            считывает json файл и возвращает его
            return data
            """
            try:
                with open(self.info_json, "r") as write_file:
                    data=json.load(write_file)

                    return data
            except:
                self.runame()
                massege.showerror("Ошибка","Ошибка чтения json файла. Возможно перезапуск решит проблему.")


        def get_name(self):
            return self.name

#функции sql




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

        def ask_user(self,title,text,fanc,list):
            """
            Запускает функцию message_yes_no проверяет ответ пользователя и если да,
            то запускает функцию переданую в аргументах

            :param title: заголовок
            :param text: сообщение
            :param fanc: фкнкция
            :param list: аргументы функции
            :return:
            """
            if self.message_yes_no(title,text):
                if list:
                    fanc(*list)
                else:
                    fanc()

        def write_table(self,):
            """
            записывает данные в бд
            :return:
            """
            if self.enter_accept==True:
                data=self.collect_info()
                self.oders_db.write_order(data[1],data[2],data[0])
                massege.showinfo("Успех","Заявка отправлена")
            else:
                massege.showerror("Ошибка","Для отправки заявки авторизируйтесь")


        def accept_order(self,id_order,who_accept):
            """
            принимает заказ
            """
            try:
                self.oders_db.update_order("accept", id_order, who_accept,None )
                massege.showinfo("Сообщение", F"Заявка принята пользователем - {who_accept}")
            except:
                massege.showerror("Ошибка","Ошибка при записи бд")

        def complit_order(self,id_order,who_accept):
            """
            завершает заказ
            """
            try:
                self.oders_db.update_order("complete", id_order, who_accept, None)
                massege.showinfo("Сообщение", F"Заявка завершена")
            except:
                massege.showerror("Ошибка", "Ошибка при записи бд")

        def check_comment(self,data,user):
            """
            проверяет можно ли остпвить коментарий
            """
            who_make=data[6]
            is_comment=data[9]
            status=data[2]
            if who_make == user and (is_comment == 'None' or is_comment == None) and status=='Взято на контроль':
                return True
            else:
                return False

        def  comment_window(self,windows,order,user):
            """
            Создает окно для комментариев
            """
            main_frame=Frame(windows,height=120,width=400,bg="green")
            lable_frame=Frame(main_frame,height=1,width=400)
            comment_frame=Frame(main_frame,heigh=3,width=400)
            but_frame=Frame(main_frame,heigh=1,width=400)
            lable_name=Label(lable_frame,text="Оставьте комментарий")
            comment_text=Text(comment_frame,heigh=3,)
            comment_text_scroll=Scrollbar(comment_frame,command=comment_text.yview)
            comment_text.config(yscrollcommand= comment_text_scroll.set)
            cancel_but=Button(but_frame,text="Отмена",command=lambda : self.ask_user(
                                    "Внимание","Вы хотите закрыть окно? Коментарий не будет добавлен если вы его не отправили!!",self.clear_comment_window,[]))
            write_but=Button(but_frame,text="Оставить коментарии",command=lambda :self.ask_user(
                                    "Внимание","Вы хотите oставить комментарий? Коментарий  будет добавлен!",self. comment_write,[comment_text,user,order]))
            main_frame.pack()
            lable_frame.pack()
            comment_frame.pack()
            but_frame.pack()
            lable_name.pack()
            comment_text.pack(side=LEFT)
            comment_text_scroll.pack(side=RIGHT,fill=Y)
            cancel_but.pack(side=LEFT)
            write_but.pack(side=LEFT)
            self.list_wiget_comment.extend([main_frame,lable_frame,comment_frame,but_frame,lable_name,comment_text,
                                            comment_text_scroll,cancel_but,write_but])

        def clear_comment_window(self):
            """
            Удаляет окно для комментариев
            """
            self.del_wiget(self.list_wiget_comment)
            self.list_wiget_comment = []
            massege.showinfo("Отмена", "Коментарий не добавлен")

        def comment_write(self,wig,user,id_order):
            """
            Получает данные из виджета и формирует их. Записывает в бд

            """
            id_=id_order[8]
            text=wig.get(1.0, END)
            if len(text)>1:
                text=f"{user} оставил комментарий:\n{text}"
                try:
                    self.oders_db.update_order("comment",id_,None,text)
                    vooo=self.oders_db.return_info_reqest(None,id_order[7],None,None,None,None)
                    orders=[order for order in vooo if order[8]==id_]
                    self.put_text(orders[0])
                    massege.showinfo("Успех","Коментарий добавлен")
                except:
                    massege.showerror("Ошибка","Комментарий не добавлен, ошибка бд")
            else:
                massege.showinfo("Внимание", "Коментарий не должен быть пустым!")








#функции для вкладки "составить заявку"
        def collect_info(self):
            """
            собирает данные по заявке для отправки в бд
            :return:
            """
            name=self.name
            themm=self.text_enter_themm.get(1.0, END)
            text=self.text_enter.get(1.0, END)
            data = self.clear_inter([(name,themm,text,)])
            return data[0]
#функции для вкладки "показать заявки"

        def count_button(self, data_ ):
            """
            Из полученных данных формирует информацию для будующих кнопок.
            :param data: данные из sql таблици
            :return:
            """


            self.list_button_info = []

            name_computer = ""
            if self.admin == "user":
                name_computer = "user"
            else:
                name_computer = "admin"
            for data in data_:
                for i in data:

                    zip = []
                    for biter in i:
                        word = ""
                        for liter in str(biter):
                            if liter != "\n":
                                word = word + liter
                        #if i[1] == self.name or name_computer == "admin":

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

            text_len=[len(len_) if len(str(len_))<=10 else 10 for len_ in text ]
            but = Button(text=f"{text[7][0:text_len[7]]} {text[3][0:text_len[3]]} {text[0][0:text_len[0]]} {text[1][0:text_len[1]]}",
                         command=lambda: self.put_text(text))
            self.list_button.append(but)

        def swow_but(self,sarch,layer):
            """
            прячет кнопки под виджетами чтобы они(кнопки) не заслоняли их

            :param sarch: рамка поиска
            :param layer: фрам с кнопками
            :return:
            """
            count=0
            for but in self.list_button:
                if sarch.winfo_y()+sarch.winfo_height()-but.winfo_height()>but.winfo_y():
                    self.list_button[count].lower(layer)
                else:
                    self.list_button[count].lift(layer)
                count+=1
        def pack_button(self,frame):
            """

            :param frame: место размещения
            :return:
            """
            for i in self.list_button:
                i.pack(in_=frame, side=TOP, fill=BOTH, expand=1, )
                self.wiwets.append(i)

        def pack_box_entery(self,frame):
            """

            :param frame: место размещения
            :return:
            """
            days = list(range(1, 32))
            months = list(range(1, 13))
            years = list(range(2021, 2099))
            status = ["Активно","Взято на контроль","Выполнено","Все"]
            row = 0
            column = 1
            list_box = self.create_wigets("Combobox", 7, (days, days, months, months, years, years,status), ())
            sarch_word = self.create_wigets("Entery", 1, (), ())[0]
            list_box.append(sarch_word)
            self.wreate_sarch_combobox(list_box)
            counter=1
            for i in list_box:
                if column == 3:
                    row += 1
                    column = 1
                i.grid(in_=frame, row=row, column=column, )
                if counter==7:
                    i.current(3)
                self.wiwets.append(i)
                column += 1
                counter+=1
            #sarch_word.grid(in_=frame, row=4, column=1, )
            self.wiwets.append(sarch_word)

        def pack_label(self,frame):
            """
            :param frame: место размещения
            :return:
            """
            row = -1
            column = 0
            step = 0
            for i in self.create_wigets("lable", 8, ("from days", "to days", "from months", "to months", " to years",
                                                     "to years","status","Word"), ()):
                if step % 2 ==0:
                    row+=1
                i.grid(in_=frame, row=row, column=column, )
                self.wiwets.append(i)
                if column==3:
                    column=0
                else:
                    column =3
                step+=1





        def put_button(self,flag):
            """
            расставляет виджеты на второй вкладке
            :return:
            """
            self.sarch_combobox = {}
            self.del_wiget(self.wiwets)
            self.wiwets = []
            heighre_ = len(self.list_button) * 26
            mane_frame=Frame(self.frame_text_oders,)
            convas = Canvas(mane_frame,)
            fremer = Frame(convas, width=0,)
            skroll = Scrollbar(convas)
            frame_sarch=Frame()
            sarch_button=Button(text="Sarch",command=lambda :self.get_info_sarch())
            fremer.pack(side=RIGHT, fill=BOTH, expand=1)

            convas.create_window((0, 0), window=fremer, width=0, height=heighre_, anchor=N + W)

            self.wiwets.extend([convas, skroll, fremer])
##########button
            if flag=="creete_button":
                self.pack_button(fremer)
###########box
            self.pack_box_entery(frame_sarch)
##########lable
            self.pack_label(frame_sarch)
#########
            skroll.config(command=convas.yview)
            skroll.pack(side=RIGHT, fill=Y, )
            convas.config(yscrollcommand=skroll.set, scrollregion=(0, 0, 0, heighre_), )
            convas.pack(side=LEFT, fill=BOTH, expand=1)
            sarch_button.grid(in_=frame_sarch, row=1, column=4)
            frame_sarch.pack(in_=self.frame_text_oders,fill=BOTH)
            mane_frame.pack(side=LEFT, fill=BOTH, expand=1,)
            skroll.bind("<Motion>", lambda event:self.swow_but(frame_sarch,fremer))
            skroll.bind("<Button-1>", lambda event: self.swow_but(frame_sarch,fremer))


            self.wiwets.extend((sarch_button,skroll,fremer,frame_sarch,mane_frame,))

        def wreate_sarch_combobox(self,list):
            """
            заполняет дикт из id жиджктов поиска заявок
            :param list:
            :return:
            """
            count=0
            for i in list:
                self.sarch_combobox[count]=i.winfo_id()
                count+=1


        def del_wiget(self,list):
            """
            отчищает список виджетов
            :return:
            """
            for i in list:
                i.destroy()


        def get_info_sarch(self):
            """
            собирает значения combobox из поиска в словарь
            :return:
            """

            names=("last_day","next_day","last_month","next_month","last_year","next_year","word","key")
            sarch_combobox_get={}
            list_login = self.count_users()
            list_info=[]

            count=0

            for i in names:
                for g in self.wiwets:
                    if g.winfo_id()==self.sarch_combobox[count]:
                        sarch_combobox_get[i]=g.get()
                        list_info.append([i,g.get()])

                count+=1
            search_obi = search_class.Search(list_info)
            search_obi=search_obi.whats_search(["last","next"],["word"],["key"])
            result=self.select_funk(search_obi)

            if list_login:
                if all(result)==False:
                    massege.showinfo("Поиск","Поиск не дал результатов")
                else:
                    massege.showinfo("Поиск",f"Результаты поиска  для пользователей {list_login}")
            else:
                massege.showerror("Ошибка","Для поиска заявок необходимо авторизироватся")


            self.click_to_notebook(result)

            #return sarch_combobox_get

        def select_funk(self,obi,):
            list_login = self.count_users()
            list_reqests=[]
            for login in list_login:
                list_reqests.append(self.oders_db.return_info_reqest(obi[0],login, obi[1]["last"], obi[1]["next"],obi[1]["word"][0]
                                                                      ,obi[1]["key"][0]))
            list_reqests=[li for li in list_reqests if len(li)]
            print(list_reqests)
            return list_reqests

        def count_users(self):
            """
            создает список логинов в завмсимости от того является пользователь одмином и авторизирован ли он
            :return: список логинов
            """
            list_users=[]
            if self.admin=="admin":
                list_users.extend(self.user_db.return_all_users())
                list_users = {name[0] for name in list_users}
            elif self.get_name()!="name_competer":
                list_users.append((self.get_name()))

            return list_users





        def create_wigets(self,types,amount,args,funk):

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
            if types=="Button":
                pass
            if types=="Entery":
                for i in range(amount):
                    return_wigets.append(Entry())
            return return_wigets

        def precondichen_list(self,list):
            """
            создает вльтернативный список с информацией о завке заменяя None на нет
            :param list:
            :return:
            """
            list_new=[]
            for i in list:
                if i =="None" or i==None:
                    list_new.append("нет")
                else:
                    list_new.append(i)
            return list_new

        def take_my_all_order(self):
            """
            возвращает все заказы из базы
            """
            list_oders=[]
            self.count_users()
            for user in self.count_users():
                list_oders.append(self.oders_db.return_info_reqest(None, user, None, None, None, None))
            return list_oders

        def put_text(self, text):
            """
            формерует и размещает текст и текстовое поле на экране
            :param text:
            :return:
            """
            order_text=self.precondichen_list(text)
            print(order_text)
            self.del_wiget(self.wiwets)
            self.wiwets=[]
            frame_but = Frame(self.frame_text_oders)
            but_back = Button(frame_but, text="Назад", command=lambda: self.click_to_notebook(self.take_my_all_order()))
            chec_statys = Button(frame_but, text="Выполнено", command=lambda: self.ask_user(
                                    "Внимание","Вы хотите завершить заявку?",self.update_status,[[text,self.name],self.complit_order]))
            chec_accept = Button(frame_but, text="Принять заявку", command=lambda: self.ask_user(
                                    "Внимание","Вы хотите принять заявку?",self.update_status,[[text,self.name],self.accept_order]))
            comment=Button(frame_but, text="Оставить коментарий", command=lambda: self.ask_user(
                                    "Внимание","Оставить коммент?",self.comment_window,[self,text,self.name]))
            tex_teria = Text(self.frame_text_oders, width=0)
            tex_teria.insert(1.0, f"Заявитель-{order_text[7]}\nТема-{order_text[0]}\nCтатус-{order_text[2]}\n"
                                  f"Заявка подана-{order_text[3][0:10]}\n"f"Заявка принята-{order_text[4]}\n"
                                  f"Заявку принял-{order_text[6]}\nЗаявка выполнена-{order_text[5]}\n"
                                  f"Cообщение:\n{order_text[1]}\n"
                                  f"Коментарий-{order_text[9]}")
            skrol_text = Scrollbar(self.frame_text_oders, command=tex_teria.yview)
            tex_teria.config(yscrollcommand=skrol_text.set)
            self.wiwets.extend((frame_but, but_back, chec_statys,chec_accept,tex_teria, skrol_text))
            but_back.pack(side=LEFT)
            if self.chec_status_orders(text, self.name)=="accept":
                chec_statys.pack(side=RIGHT)
            elif self.chec_status_orders(text, self.name)=="not_accept":
                chec_accept.pack(side=RIGHT)
            elif self.chec_status_orders(text, self.name)=="not_make":
                pass
            if self.check_comment(text,self.name):
                comment.pack(side=RIGHT)
            frame_but.pack(side=TOP)
            tex_teria.pack(side=LEFT, fill=BOTH, expand=1)
            skrol_text.pack(side=RIGHT, fill=Y)

        def chec_status_orders(self, order,user):
            """
            на основе данных о заказе и юзере, опредиляет какой статус заказа
            return status статус заказа
            """
            who_i=user
            who_start_order=order[7]
            status_order=order[2]
            status=""
            if self.admin == "admin" and who_i != who_start_order and status_order == "Активно":
                status="not_accept"
            elif who_i == who_start_order and status_order == "Взято на контроль":
                status = "accept"
            else:
                status = "not_make"
            return status



        def update_status(self,data,fanc):
            """
            обновляет статус заказа в таблице и для кнопок
            :param data:
            :return:
            """
            id_order = data[0][8]
            who_accept = data[1]
            fanc(id_order,who_accept)

            self.create_button()
            data_new=self.oders_db.return_info_reqest(None,data[0][7],None,None,None,None)
            data_new=[i for i in data_new if int(data[0][8]) in i]
            self.put_text(data_new[0])


        def message_yes_no(self,title,message_):
            """
            создает окно с вопросом и возвращает ответ
            :param title: название окна
            :param message_: текст вопроса
            :return: ответ
            """
            answer=massege.askyesno(title,message_)
            return answer

        def click_to_notebook(self ,list):

            self.count_button(list)
            self.create_button()
            self.put_button("creete_button")


        def call_of_admin(self, ):
            """
            если режим админа запужен иледит за бд и выдает сообщение  при ее изменении
            :return:
            """
            #len_sql=len(self.print_table())
            #while True:
                #pass
                #time.sleep(2)
                #if self.admin=="admin" and len(self.print_table())>len_sql:
                    #len_sql=len(self.print_table())
                    #list_info=self.print_table()[0]
                    #info=[list_info[1],list_info[2]]
                    #massege.showerror("Внимание",f"Новая заявка:\n заявитель-{info[0]} тема-{info[1]}")






winner=Win()
winner.set_parametrs()
winner.pack_widgets()
winner.user_db.create_table()
winner.oders_db.create_table()

winner.hi_client()
cot=threading.Thread(target=winner.call_of_admin,daemon = True)
cot.start()
winner.mainloop()
