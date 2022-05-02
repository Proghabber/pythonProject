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





tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
frame_info=Frame(tab1)
klient = Label(frame_info,text="Имя клиента - " )
text_info = definity.chenge_wiget()

date_label = Label(frame_info,text="Дата сегодня - " )
date_now=Label(frame_info,text=date)
text_enter=Text(tab1)
scrol_text = Scrollbar(tab1,command=text_enter.yview)



tabControl.place(relx=0, rely=0,relwidth=1, relheight=1 )
tab2.place()
tab1.place()
frame_info.pack(anchor=S)

date_label.pack(side=LEFT )
date_now.pack(side=LEFT )
klient.pack(side=LEFT )
for i in text_info:
    i.pack(in_=frame_info,side=LEFT)
text_enter.pack(anchor=W,expand=1,fill=BOTH,side=LEFT)
scrol_text.pack(anchor=E,fill=Y,side=RIGHT)
text_enter.config(yscrollcommand=scrol_text.set)








#definity.show_widget([frame],"show")

window.mainloop()