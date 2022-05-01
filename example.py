import datetime
from tkinter import *
from tkinter import ttk
import definity

window = Tk()
window.title("РџСЂРѕРіСЂР°РјРјР° РґР»СЏ РїРѕРґСЃС‡РµС‚Р° СЂР°Р±РѕС‡РёС… С‡Р°СЃРѕРІ")
width = 600
height = 500
info = "РџСЂРёРІРµС‚, РІС‹Р±РµСЂРё РґРµР№СЃС‚РІРёРµ"
window.geometry(f"{width}x{height}")

data_now = datetime.datetime.today()
data_now_format = definity.kalendwr([data_now.year, data_now.month, data_now.day])
data_now_format_text = (data_now_format[0], data_now_format[1], data_now_format[2])
seleckt_data = ["РІС‹Р±СЂaС‚СЊ", data_now_format_text]
seleckt_works = definity.full_seleckt_wigets(["СѓРєР°Р¶Рё"], "work")
selekt_days = ["РІС‹Р±СЂaС‚СЊ","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
               "18", "19", "20", "21", "22",
               "23", "24", "25", "26", "27", "28", "29", "30", "31"]
select_months = ["РІС‹Р±СЂaС‚СЊ","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
select_yars = definity.full_seleckt_wigets(
    ["СѓРєР°Р¶Рё", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031"], "year")
select_hours = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
                "18", "19", "20", "21", "22", "23", "24"]

definity.find_derectory()
conwas=Canvas(window,width=width, height=height,bg='white')
conwas.create_rectangle(3,18,597,150,outline="blue",width=2)
conwas.create_rectangle(3,189,597,268,outline="red",width=2)

inform_to_process = Label(text=info, )

name1 = Label(text="РРЅС‚РµСЂС„РµР№СЃ РІРІРѕРґР° РґР°РЅРЅС‹С…",bg="blue",fg="white")
name2 = Label(text="РРЅС‚РµСЂС„РµР№СЃ РІС‹РІРѕРґР° РґР°РЅРЅС‹С…",bg="red",fg="white")
name3 = Label(text="Р”Р°С‚Р°")
name4 = Label(text="Р”РѕР»Р¶РЅРѕСЃС‚СЊ")
name5 = Label(text="Р”РµРЅСЊ")
name6 = Label(text="РњРµСЃСЏС†")
name7 = Label(text="Р“РѕРґ")
name8 = Label(text="Р§Р°СЃ")
name10 = Label(text="Р”РѕР»Р¶РЅРѕСЃС‚СЊ")
name11 = Label(text="Р”РµРЅСЊ")
name12 = Label(text="РњРµСЃСЏС†")
name13 = Label(text="Р“РѕРґ")
frame = Frame()

text_info = Text(frame, width=70, height=9,bg="green",fg="yellow")
scrol_text = Scrollbar(frame, command=text_info.yview,)

select_date1 = ttk.Combobox(values=seleckt_data)
select_date1.current(1)

select_date2 = ttk.Combobox(values=seleckt_works)
select_date2.current(0)
select_day = ttk.Combobox(values=selekt_days[1:], state="disable")
select_day.current(0)
select_month = ttk.Combobox(values=select_months[1:], state="disable")
select_month.current(0)
select_year = ttk.Combobox(value=select_yars, state="disable")
select_year.current(0)
select_hour = ttk.Combobox(values=select_hours)
select_hour.current(0)
select_work = ttk.Combobox(values=seleckt_works)
select_work.current(0)
select_work.bind("<Button-1>", lambda e: select_work.configure(values=seleckt_works))
select_day1 = ttk.Combobox(values=selekt_days)
select_day1.current(0)
select_month1 = ttk.Combobox(values=select_months)
select_month1.current(0)
select_year1 = ttk.Combobox(values=select_yars)
select_year1.bind("<Button-1>", lambda e: select_year1.configure(values=select_yars))
select_year1.current(0)

button1 = Button(text="РџСЂРѕРІРµСЂРёС‚СЊ", command=lambda: definity.main_count(
    [select_date1, select_date2, select_day, select_month, select_year, select_hour, seleckt_works, select_yars,
     inform_to_process]))
button2 = Button(text="РЈСЃС‚Р°РЅРѕРІРёС‚СЊ", command=lambda: definity.writ_info_in_file(["work", "year", "data"], inform_to_process))
button3 = Button(text="РџРѕР»СѓС‡РёС‚СЊ", command=lambda: definity.data_colleckt([select_work, select_year1, select_month1,
                                                                          select_day1], text_info, inform_to_process))
button4 = Button(text="РЎСѓРјРјР° С‡Р°СЃРѕРІ", command=lambda: definity.count_hours(text_info, inform_to_process))
button5 = Button(text="РЈРґР°Р»РёС‚СЊ", command=lambda: definity.del_information_in_file(inform_to_process))

name1.place(x=10, y=400 / 6)
name2.place(x=10, y=400 / 2 + 38)
name3.place(x=10, y=400 / 4)
name4.place(x=10, y=400 / 4 + 40)
name5.place(x=170, y=400 / 4)
name6.place(x=170, y=400 / 4 + 20)
name7.place(x=170, y=400 / 4 + 40)
name8.place(x=170, y=400 / 4 + 60)
name10.place(x=10, y=400 / 4 + 160)
name11.place(x=200, y=400 / 4 + 160)
name12.place(x=200, y=400 / 4 + 180)
name13.place(x=200, y=400 / 4 + 200)


select_date1.place(x=10, y=400 / 4 + 20)
select_date2.place(x=10, y=400 / 4 + 60)

select_day.place(x=215, y=400 / 4)
select_month.place(x=215, y=400 / 4 + 20)
select_year.place(x=215, y=400 / 4 + 40)
select_hour.place(x=215, y=400 / 4 + 60)
select_work.place(x=10, y=280)
select_day1.place(x=250, y=400 / 4 + 160)
select_month1.place(x=250, y=400 / 4 + 180)
select_year1.place(x=250, y=400 / 4 + 200)

frame.place(x=0, y=330)
text_info.pack(side=LEFT)
scrol_text.pack(side=RIGHT, fill=Y)

button1.place(x=370, y=400 / 4)
button2.place(x=370, y=400 / 4 + 40)
button3.place(x=400, y=400 / 4 + 160)
button4.place(x=400, y=400 / 4 + 190)
button5.place(x=500, y=400 / 4 + 160)
select_date1.bind("<FocusIn>",
                  lambda e: definity.block_seleckt_widget(select_date1, [select_day, select_month, select_year]))
text_info.config(yscrollcommand=scrol_text.set)
inform_to_process.pack(side=TOP, pady=20)
conwas.pack()
window.mainloop()
