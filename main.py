from tkinter import *
from tkinter import ttk
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
#definity.chenge_wiget(window,"no")
#создать заявку
#make_oder=definity.WidgetShow()


#посмотреть заявку








#надписи






#кнопки

#боксы
tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)





tabControl.add(tab1, text='Составить заявку')
tabControl.add(tab2, text='Посмотреть заявки')
frame_info=Frame(tab1)
frame_text=Frame(tab1)
frame_sent=Frame(tab1)
klient = Label(frame_info,text="Имя клиента - " )

date_label = Label(frame_info,text="Дата сегодня - " )
date_now=Label(frame_info,text=date)

text_enter=Text(tab1)
scrol_text = Scrollbar(tab1,command=text_enter.yview)
batton_send_info=Button(frame_sent,text="Отправить")



tabControl.place(relx=0, rely=0,relwidth=1, relheight=1 )
tab2.place()
tab1.place()
frame_info.pack(anchor=W)
frame_sent.pack(anchor=W,pady=2)
batton_send_info.pack()
date_label.pack(side=LEFT,ipadx=10 )
date_now.pack(side=LEFT,ipadx=10 )
klient.pack(side=LEFT ,ipadx=10)
#for i in text_info:
   # i.pack(in_=frame_info,side=LEFT,ipadx=10)
sio=definity.info_to_enter(frame_info)
sio.chenge_wiget()

frame_text.pack(expand=1,fill=BOTH,side=LEFT,)
text_enter.pack(in_=frame_text,anchor=NW,expand=1,fill=BOTH,side=LEFT)
batton_send_info.pack(anchor=N,side=TOP)
scrol_text.pack(in_=frame_text,anchor=NE,fill=Y,side=RIGHT)
text_enter.config(yscrollcommand=scrol_text.set)


topic=definity.return_sql()


frame_tab2=Frame(tab2)
frame_select=Frame(frame_tab2)
skroll_button=ttk.Combobox(values=definity.return_topic(topic))


skroll_button.pack(in_=frame_select,anchor=NW,expand=1,fill=BOTH,side=LEFT)
frame_select.pack(fill=X,)

frame_text_oders=Frame(frame_tab2)
text_oders=Text(frame_text_oders)
scrol_text_oders=Scrollbar(frame_text_oders)
text_oders.pack(in_=frame_text_oders,anchor=NE,expand=1,fill=X,side=LEFT)
scrol_text_oders.pack(in_=frame_text_oders,fill=Y,side=RIGHT)
text_oders.config(yscrollcommand=scrol_text_oders.set)
frame_text_oders.pack(anchor=NW,expand=1,fill=BOTH,)
frame_tab2.place(relx=0, rely=0,relwidth=1, relheight=1 )
frame_tab2.bind("<Enter>", lambda e: definity.return_info_in_sql(skroll_button.get(),topic,text_oders))
#definity.show_widget([frame],"show")

window.mainloop()