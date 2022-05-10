import json
from pathlib import Path
from tkinter import *
from tkinter import ttk

import sql

class info_to_enter():
    """класс занимается приветствием пользователя и получением его именя если оно не известно

    """
    def __init__(self,wig):
        self.list_wiget=[]
        self.name=""
        self.place=wig

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
        опредиляет сохранено имя в файле, ида бто дает лабел с именем на табло, иначе запускает скрспт получения имени
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





def kalendwr(a: list[int]) -> list[str]:
    """получает список интов и преобразует в список строк и если получился один знак ,то добавляет перед ним 0"""
    b = []
    for i in a:
        i = str(i)

        if len(i) < 2:
            i = "0" + i
        b.append(i)
    return b












def count_frame_button():
    k = 1
    list_name=[]
    try:
        list_button=open("keep_oders.py", encoding='utf-8')
        read_list_button=list_button.readlines()
        json_list_button=json.loads(read_list_button[0])
        for i in json_list_button:
            list_name.append(i)

            k+=1
        list_button.close()
    except:
        print("false")
    return (k,list_name)




def show_widget(list_widget: list,flag):

        if flag=="show":
            list_widget[0].place_forget()

        else:
            list_widget[0].place()

def return_sql():
    ret=sql.print_table()
    return ret

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





