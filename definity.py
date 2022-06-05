import json
from pathlib import Path
from tkinter import *
from tkinter import ttk


import sqlite3

class info_to_enter():
    """класс занимается приветствием пользователя и получением его именя если оно не известно

    """
    def __init__(self,wig):
        self.list_wiget=[]
        self.name=""
        self.place=wig
    def get_name(self):
        return  self.name

    def no_name(self,):
        """
        если имени нет то создает виджеты для получения имени
        :return:
        """
        self.list_wiget=[]
        text_info = Text(width=10, height=1, bg="white", fg="black")
        klient_name = Button(text="Установить",command= lambda:self.know_name())
        text_info.pack(in_=self.place, side=LEFT, ipadx=10)
        klient_name.pack(in_=self.place, side=LEFT, ipadx=10)
        self.list_wiget.append(text_info)
        self.list_wiget.append(klient_name)



    def know_name(self,):
        """
        когда имя введино(нажата кнопка), получает значение поля и удаляет старые виджеты
        :return:
        """
        for i in self.list_wiget:
                if i.winfo_class()=="Text":
                    self.name=i.get(1.0, END)[0:-1]
                i.destroy()
        text=Label(text=self.name)
        text.pack(in_=self.place, side=LEFT, ipadx=10)
        self.runame()


    def runame(self,):
        """
        записывает полученое имя в json файл
        :return:
        """
        info = {"name_competer": self.name}
        try:
            with open("info.json", "w") as write_file:
                json.dump(info, write_file)
        except:
            pass

    def chenge_wiget(self,):
        """
        опредиляет сохранено имя в файле, если да то дает лабел с именем на табло, иначе запускает скрспт получения имени
        """
        try:
            with open("info.json", "r") as read_file:
                info1 = json.load(read_file)
                name_competer = info1["name_competer"]
                self.name = name_competer
                text = Label(text=name_competer)
                text.pack(in_=self.place, side=LEFT, ipadx=10)

        except:
            self.no_name()
class work_sql():
    def __init__(self):
        self.path="base_data/sik.db"

    def create_bd(self):
        with sqlite3.connect(self.path) as content:
            cursor = content.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS articles(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client VARCHAR,
            topic VARCHAR,
            text TEXT,
            status TEXT
            )""")

    def print_table(self):
        with sqlite3.connect(self.path) as content:
            cursor = content.cursor()
            cursor.execute("SELECT *FROM ARTICLES")
            return cursor.fetchall()

    def write_table(self,data):
        with sqlite3.connect(self.path) as content:
            cursor = content.cursor()
            cursor.execute("SELECT *FROM ARTICLES")
            cursor.executemany("INSERT INTO articles(client, topic, text, status) VALUES(?,?,?,?)", data)

    def update_info(self,data):
        with sqlite3.connect(self.path) as content:
            cursos=content.cursor()
            cursos.execute("SELECT id  FROM articles")
            cursos.execute("UPDATE  articles  SET status = 'Исполнено' WHERE id = (?)",[data[0]])



class Textery():
    """
    Класс отвечает за вкладку 'посмотреть заявки' и создает конвас со списоком кнопок заявок ,а также текстовое поле для
    каждой заявки.Размещает эти полотна на экране меняя их между собой.
    """
    def __init__(self, wig,sql):
        self.place=wig
        self.sql=sql
        self.list_button_info=[]
        self.list_button=[]
        self.wiwets=[]

    def count_button(self,data:list):
        """
        Из полученных данных формирует информацию для будующих кнопок.
        :param data: данные из sql таблици
        :return:
        """
        self.list_button_info=[]
        for i in data:
            zip=[]
            for ty in i :
                ty=str(ty)
                if '\n' in ty:
                    ty=ty[0:-1]
                zip.append(ty)
            self.list_button_info.append(zip)


    def create_button(self,):
        """
        Перебирает инфу для кнопок и запускает функцию создания кнопки
        :return:
        """
        self.list_button=[]
        for i in self.list_button_info:
            self.create_but(i)

    def create_but(self,text):
        """
        создают кнопку и функцию к ней прекрепляет, ложет ее в список
        :param text:
        :return:
        """
        if len(text[3])>10:
            len_mass=10
        else:
            len_mass=len(text[3])
        but = Button(text=f"{text[0]} {text[1]} {text[2]}-{text[3][0:len_mass]}", command=lambda: self.put_text(text))
        self.list_button.append(but)

    def put_button(self,):
        """
        расставляет кнопки на экране
        :return:
        """
        self.del_wiget()
        heighre_=len(self.list_button)*26
        convas = Canvas(self.place,height=heighre_,width=0)
        fremer = Frame(convas,width=0)
        skroll = Scrollbar(convas)
        fremer.pack(side=RIGHT, fill=BOTH, expand=1)
        convas.create_window((0, 0), window=fremer,width=0, height=heighre_, anchor=N + W)
        self.wiwets.extend([convas,skroll,fremer])
        for i in self.list_button:
            i.pack(in_=fremer,side=TOP,fill=BOTH,expand=1)
        skroll.config(command=convas.yview)
        skroll.pack(side=RIGHT,fill=Y,)
        convas.config(yscrollcommand=skroll.set, scrollregion=(0, 0, 0, heighre_), )
        convas.pack(side=LEFT,fill=BOTH,expand=1)


    def del_wiget(self):
        """
        отчищает список виджетов
        :return:
        """
        for i in self.wiwets:
            i.pack_forget()

    def put_text(self,text):
        """
        формерует и размещает текст и текстовое поле на экране
        :param text:
        :return:
        """
        self.del_wiget()
        frame_but = Frame(self.place)
        but_back=Button(frame_but,text="Назад",command=lambda:self.put_button())
        chec_statys=Button(frame_but,text="Выполнено",command=lambda:self.update_status(text))
        tex_teria=Text(self.place,width=0)
        tex_teria.insert(1.0, f"Заявитель-{text[1]}\nТема-{text[2]}\nCтатус-{text[4]}\nCообщение:\n{text[3]}")
        skrol_text=Scrollbar(self.place,command=tex_teria.yview)
        tex_teria.config(yscrollcommand=skrol_text.set)
        self.wiwets.extend((frame_but,but_back,chec_statys,tex_teria,skrol_text))
        but_back.pack(side=LEFT)
        chec_statys.pack(side=RIGHT)
        frame_but.pack(side=TOP)
        tex_teria.pack(side=LEFT,fill=BOTH,expand=1)
        skrol_text.pack(side=RIGHT,fill=Y)

    def update_status(self,data) :
        """
        обновляет статус заказа в таблице и для кнопок
        :param data:
        :return:
        """
        self.sql.update_info(data)
        self.create_button()
        data[4]="Исполнено"
        self.put_text(data)









def kalendwr(a: list[int]) -> list[str]:
    """получает список интов и преобразует в список строк и если получился один знак ,то добавляет перед ним 0"""
    b = []
    for i in a:
        i = str(i)

        if len(i) < 2:
            i = "0" + i
        b.append(i)
    return b


def chenge_wiget_info(wig,data):
    wig.config(value=data)



def return_topic(sql):
    ret_list=[]
    for i in sql:
        ret_list.append(i[2])
    return ret_list

def return_info_in_sql(topic,sql,wig):
    text=""
    for i in sql:
        if topic in i:
            text=f"клиент- {i[1]}\nстатус- {i[4]} \nОписание проблемы:\n{i[3]}"
        else:
            if not text:
                text = ""
    wig.delete(1.0, END)
    wig.insert(1.0,text)





