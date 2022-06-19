from tkinter import *
from tkinter import ttk
import threading
import datetime
import json
import definity
window=Tk()
window.title("Программа оформления заявок")
width = 660
height = 500


window.geometry(f"{width}x{height}")
date=datetime.datetime.today()
date=definity.kalendwr([date.day, date.month,date.year])

#поля


#посмотреть заявку

#надписи

#кнопки

#боксы
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


#первая вкладка
tabControl.add(tab1, text='Составить заявку')
frame_info=Frame(tab1,height=20)
frame_text=Frame(tab1)
frame_sent=Frame(tab1,height=20)
klient = Label(frame_info,text="Имя клиента - " )

date_label = Label(frame_info,text="Дата сегодня - " )
date_now=Label(frame_info,text=date)

text_enter=Text(frame_text,width=0, )
text_enter.insert(INSERT,"Cообщение")
text_enter_themm=Text(frame_sent,height=1)
text_enter_themm.insert(INSERT, "Тема",)

scrol_text = Scrollbar(tab1,command=text_enter.yview)
batton_send_info=Button(frame_sent,text="Отправить",command= lambda:sql_table.write_table([(meet.get_name(),text_enter_themm.get(1.0, END),text_enter.get(1.0, END),"актуально")]))


frame_info.pack(anchor=W)
frame_sent.pack(anchor=W,pady=2,expand=0,fill=X)
date_label.pack(side=LEFT,ipadx=10 )
date_now.pack(side=LEFT,ipadx=10 )
frame_text.pack(expand=1,fill=BOTH,side=LEFT,)
text_enter.pack(in_=frame_text,anchor=NW,expand=1,fill=BOTH,side=LEFT,)
text_enter_themm.pack(anchor=N,expand=1,fill=X,side=BOTTOM)
batton_send_info.pack(side=LEFT)
scrol_text.pack(in_=frame_text,anchor=NE,fill=Y,side=RIGHT)
text_enter.config(yscrollcommand=scrol_text.set)
klient.pack(side=LEFT ,ipadx=10)
meet=definity.info_to_enter(frame_info)
meet.chenge_wiget()
tab1.place()
sql_table=definity.work_sql(meet.name,meet.path)
sql_table.create_bd()
tabControl.add(tab2, text='Посмотреть заявки')

#вкладка2
frame_tab2=Frame(tab2)
frame_text_oders=Frame(frame_tab2,)
buttib=definity.Textery(frame_text_oders,sql_table,meet.name)

frame_text_oders.pack(anchor=NW,expand=1,fill=BOTH,)
frame_tab2.place(relx=0, rely=0,relwidth=1, relheight=1 )




tab2.place()
tabControl.place(relx=0, rely=0,relwidth=1, relheight=1 )
tabControl.bind('<Button-1>',lambda e: buttib.click_to_notebook())

window.mainloop()