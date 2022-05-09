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
text_info = definity.chenge_wiget()


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
for i in text_info:
    i.pack(in_=frame_info,side=LEFT,ipadx=10)

frame_text.pack(expand=1,fill=BOTH,side=LEFT,)
text_enter.pack(in_=frame_text,anchor=NW,expand=1,fill=BOTH,side=LEFT)
batton_send_info.pack(anchor=N,side=TOP)
scrol_text.pack(in_=frame_text,anchor=NE,fill=Y,side=RIGHT)
text_enter.config(yscrollcommand=scrol_text.set)




frame_button=Frame(tab2)
skroll_button=Text(tab2)
list_result=definity.count_frame_button()
list_button=[]
for i in list_result[1]:
    list_button.append(Button(text=i))
print(list_result[0]*20)
skroll_button.place(x=0,y=0,relwidth=1,height=list_result[0]*20)
k=0
for i in list_button:
    i.place_configure(in_=skroll_button,relwidth=1)
    i.place(y=k)
    k+=25






#definity.show_widget([frame],"show")

window.mainloop()