import json
from pathlib import Path
from tkinter import *
from tkinter import ttk
class WidgetShow():
    def __init__(self,):

        self.y = 0
        self.septil=[]
        self.frame=Frame()
        self.frame1=Frame()
        self.text_info = Text(bg="green",fg="yellow")
        self.text_info1 = Canvas()
        self.scrol_text = Scrollbar()
        self.scrol_text1 = Button(text="0",command=lambda: self.rio(self.septil,25))
        self.scrol_text2 = Button(text="0", command=lambda: self.rio(self.septil, -25))
        self.oder_send=Button(text="Отправить-")

    def rio(self,list,stepe):
        info_convas=self.text_info1.place_info()
        geo_convas=self.text_info1.winfo_height()


        step=stepe+self.y
        for i in list:
            i.place(in_=self.frame1,y=step)
            info=i.place_info()
            print(info["y"],info_convas["y"],geo_convas)
            if int(info["y"]) > int(info_convas["y"])+int(geo_convas)-25 or int(info["y"])+25 < int(info_convas["y"]):
                i.place_forget()
            step += stepe
            if stepe==0:
                step+= 25
        self.y+=stepe
        print(15)


    def show_make_oder(self):
        self.show_watche_oders()



        self.frame.place(relx=0.0, rely=0.40, relwidth=1, relheight=0.60)
        self.text_info.pack(in_=self.frame,expand=True,fill=BOTH,side=LEFT)
        self.scrol_text.pack(in_=self.frame,fill=Y,side=RIGHT)
        self.oder_send.place(in_=self.text_info,anchor=SW)

    def show_watche_oders(self,):
        self.oder_send.place_forget()
        self.frame1.place(relx=0.0, rely=0.20, relwidth=1, relheight=0.20)
        self.text_info1.place(in_=self.frame1,relwidth=1, relheight=1 )
        self.scrol_text1.pack(in_=self.frame1,anchor=E,fill=Y,expand=True)
        self.scrol_text2.pack(in_=self.frame1,anchor=E,fill=Y,expand=True)

        for i in range(50):
            m=Button(text=i)
            self.septil.append(m)
        self.text_info1.config()
        self.rio(self.septil,0)












def kalendwr(a: list[int]) -> list[str]:
    """получает список интов и преобразует в список строк и если получился один знак ,то добавляет перед ним 0"""
    b = []
    for i in a:
        i = str(i)

        if len(i) < 2:
            i = "0" + i
        b.append(i)
    return b

def chenge_wiget():

    try:
        info = open("info.py", encoding='utf-8')
        inf = info.readlines()
        info1 = json.loads(inf[0])
        name_competer = info1["name_competer"]
        check = 1
        info.close()
    except:
        name_competer = False
        check = 0

    if check == 1:
        text_info = Label(text=name_competer)
        return [text_info]


    else:
        text_info = Text( width=10, height=1, bg="white", fg="black")
        klient_name = Button(text="Установить")
        return [text_info,klient_name]


def show_widget(list_widget: list,flag):

        if flag=="show":
            list_widget[0].place_forget()

        else:
            list_widget[0].place()






