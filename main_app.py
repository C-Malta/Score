
from tkinter import *
from tkinter import ttk
import tkinter as tk
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from general_functions import *
import os 




def update():

    user_name_label.config(text="Name: "+"{val}".format(val= gather_user_data()[0]))
    user_age_label.config(text="Age: " + "{val}".format(val=gather_user_data()[1]))
    user_sex_label.config(text="Sex: " + "{val}".format(val=gather_user_data()[2]))
    user_height_label.config(text="Height: " + "{val}".format(val=gather_user_data()[3]))

    waist_circ_label.config(text="Waist Circumference: "+"{val}".format(val= gather_health_data()[0]))
    hba1c_label.config(text="HbA1c: "+"{val}".format(val= gather_health_data()[1]))
    hdl_label.config(text="HDL: "+"{val}".format(val= gather_health_data()[2]))
    ldl_label.config(text="LDL: "+"{val}".format(val= gather_health_data()[3]))
    tg_label.config(text="Triglycerides: "+"{val}".format(val= gather_health_data()[4]))
    fglucose_label.config(text="Fasting Glucose: "+"{val}".format(val= gather_health_data()[5]))
    finsulin_label.config(text="Fasting Insulin: "+"{val}".format(val= gather_health_data()[6]))
    vitd_label.config(text="Vitamin D: "+"{val}".format(val= gather_health_data()[7]))
    totalt_label.config(text="Total Testosterone: "+"{val}".format(val= gather_health_data()[8]))

    hundred_m_sprint_label.config(text="100m Sprint: "+"{val}".format(val= gather_fitness_data()[0]))
    marathon_label.config(text="Marathon: "+"{val}".format(val= gather_fitness_data()[1]))
    deadlift_label.config(text="Deadlift: "+"{val}".format(val= gather_fitness_data()[2]))
    squat_label.config(text="Squat: "+"{val}".format(val= gather_fitness_data()[3]))
    bench_press_label.config(text="Bench Press: "+"{val}".format(val= gather_fitness_data()[4]))
    overhead_press_label.config(text="Overhead Press: "+"{val}".format(val= gather_fitness_data()[5]))
    chin_up_label.config(text="Chin Up: "+"{val}".format(val= gather_fitness_data()[6]))
    dead_hang_label.config(text="Dead Hang: "+"{val}".format(val= gather_fitness_data()[7]))
    vo2_label.config(text="VO2 Max: "+"{val}".format(val= gather_fitness_data()[8]))

    total_sats_or_btc_label.config(text="Total Sats: "+"{val}".format(val= gather_finance_data()[0]))
    monthly_income_label.config(text="Monthly Income: "+"{val}".format(val= gather_finance_data()[1]))
    monthly_expenses_label.config(text="Monthly Expenses As % Of Income: "+"{val}".format(val= gather_finance_data()[2]))
    debt_label.config(text="Debt: "+"{val}".format(val= gather_finance_data()[3]))
    assets_value_label.config(text="Assets Value: "+"{val}".format(val= gather_finance_data()[4]))

    

    

    mainroot.after(1000, update)


mainroot = Tk()
mainroot.title('Score')
mainroot.geometry("577x590")


style = ttk.Style(mainroot)
style.configure('lefttab.TNotebook', tabposition='wn')

#tab manager and primary tabs creation

tabs = ttk.Notebook(mainroot)
tabs.pack(fill='both', expand=1)

first_frame = Frame()
second_frame = Frame()
third_frame = Frame()
fourth_frame = Frame()
first_frame.pack(fill='both', expand=1)
second_frame.pack(fill='both', expand=1)
third_frame.pack(fill='both', expand=1)
fourth_frame.pack(fill='both', expand=1)

tabs.add(first_frame, text="        User        ")
tabs.add(second_frame, text="        Health        ")
tabs.add(third_frame, text="        Fitness        ")
tabs.add(fourth_frame, text="        Finance        ")


#subtabs for frame 2

subtabs2 = ttk.Notebook(second_frame, style='lefttab.TNotebook')
subtabs2.pack(fill='both', expand=1)

subtabs2_frame1 = Frame(subtabs2)
subtabs2_frame1.pack(fill="both", expand=1)
subtabs2_frame2 = Frame(subtabs2)
subtabs2_frame2.pack(fill="both", expand=1)

subtabs2.add(subtabs2_frame1, text="Current")
subtabs2.add(subtabs2_frame2, text="Graphs")


#create mainframe

main_frame = tk.Frame(subtabs2_frame2)
main_frame.pack(fill='both', expand=1)

#create frame that expands endlessly
tkcanvas = tk.Canvas(main_frame)
tkcanvas.pack(side='left', fill='both', expand=1)

#create scrollbar

my_scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=tkcanvas.yview)
my_scrollbar.pack(side='right', fill='y')


#configure the canvas 

tkcanvas.configure(yscrollcommand=my_scrollbar.set)
tkcanvas.bind('<Configure>', lambda e: tkcanvas.configure(scrollregion = tkcanvas.bbox('all')))

#create inner canvas frame


def updateif():
    
    x = creation_date_list()
    wl = get_element_list('health','waist_circumference')
    hb = get_element_list('health','hba1c')
    hdl = get_element_list('health','hdl')
    ldl = get_element_list('health','ldl')
    tg = get_element_list('health','triglycerides')
    fg = get_element_list('health','fasting_glucose')
    fi = get_element_list('health','fasting_insulin')
    vd = get_element_list('health','vitamin_d')
    tt = get_element_list('health','total_testosterone')
    for item in inner_frame.winfo_children():
        item.destroy()
    health_graphs(x, wl, hb, hdl, ldl, tg, fg, fi, vd, tt)
    inner_frame.after(30000, updateif)

inner_frame = tk.Frame(tkcanvas)


def health_graphs(x, wl, hb, hdl, ldl, tg, fg, fi, vd, tt):

    #create window in canvas

    tkcanvas.create_window((0,0), window=inner_frame, anchor='nw')


    #create sub_inner_frame

    sub_inner_frame = tk.Frame(inner_frame)
    sub_inner_frame.pack(fill='both', expand=1)

    #create label naming the graph

    labelt = tk.Label(sub_inner_frame, text='Waist Circumference')
    labelt.pack()


    #create figure that fills the subframe
    f = figure.Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(x, wl)

    canvas = FigureCanvasTkAgg(f, master=sub_inner_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    
    toolbar = NavigationToolbar2Tk(canvas, sub_inner_frame)
    toolbar.update()

    #create sub_inner_frame2

    sub_inner_frame2 = tk.Frame(inner_frame)
    sub_inner_frame2.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame2, text='HbA1c Levels')
    label.pack()

    #create figure, canvas, and toolbar 2


    f2 = figure.Figure(figsize=(5, 5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(creation_date_list(), hb)


    canvas2 = FigureCanvasTkAgg(f2, master=sub_inner_frame2)
    canvas2.draw()
    canvas2.get_tk_widget().pack()

    toolbar2 = NavigationToolbar2Tk(canvas2, sub_inner_frame2)
    toolbar2.update()



    #create sub_inner_frame3

    sub_inner_frame3 = tk.Frame(inner_frame)
    sub_inner_frame3.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame3, text='HDL Cholesterol Levels')
    label.pack()

    #create figure, canvas, and toolbar 3
    f3 = figure.Figure(figsize=(5, 5), dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(creation_date_list(), hdl)

    canvas3 = FigureCanvasTkAgg(f3, master=sub_inner_frame3)
    canvas3.draw()
    canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar3 = NavigationToolbar2Tk(canvas3, sub_inner_frame3)
    toolbar3.update()


    #create sub_inner_frame4

    sub_inner_frame4 = tk.Frame(inner_frame)
    sub_inner_frame4.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame4, text='LDL Cholesterol Levels')
    label.pack()

    #create figure, canvas, and toolbar 4
    f4 = figure.Figure(figsize=(5, 5), dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(creation_date_list(), ldl)

    canvas4 = FigureCanvasTkAgg(f4, master=sub_inner_frame4)
    canvas4.draw()
    canvas4.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar4 = NavigationToolbar2Tk(canvas4, sub_inner_frame4)
    toolbar4.update()

    #create sub_inner_frame5

    sub_inner_frame5 = tk.Frame(inner_frame)
    sub_inner_frame5.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame5, text='Triglycerides Levels')
    label.pack()

    #create figure, canvas, and toolbar 5
    f5 = figure.Figure(figsize=(5, 5), dpi=100)
    a5 = f5.add_subplot(111)
    a5.plot(creation_date_list(), tg)

    canvas5 = FigureCanvasTkAgg(f5, master=sub_inner_frame5)
    canvas5.draw()
    canvas5.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar5 = NavigationToolbar2Tk(canvas5, sub_inner_frame5)
    toolbar5.update()

    #create sub_inner_frame6

    sub_inner_frame6 = tk.Frame(inner_frame)
    sub_inner_frame6.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame6, text='Fasting Glucose Levels')
    label.pack()

    #create figure, canvas, and toolbar 6
    f6 = figure.Figure(figsize=(5, 5), dpi=100)
    a6 = f6.add_subplot(111)
    a6.plot(creation_date_list(), fg)

    canvas6 = FigureCanvasTkAgg(f6, master=sub_inner_frame6)
    canvas6.draw()
    canvas6.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar6 = NavigationToolbar2Tk(canvas6, sub_inner_frame6)
    toolbar6.update()

    #create sub_inner_frame7

    sub_inner_frame7 = tk.Frame(inner_frame)
    sub_inner_frame7.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame7, text='Fasting Insulin Levels')
    label.pack()

    #create figure, canvas, and toolbar 7
    f7 = figure.Figure(figsize=(5, 5), dpi=100)
    a7 = f7.add_subplot(111)
    a7.plot(creation_date_list(), fi)

    canvas7 = FigureCanvasTkAgg(f7, master=sub_inner_frame7)
    canvas7.draw()
    canvas7.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar7 = NavigationToolbar2Tk(canvas7, sub_inner_frame7)
    toolbar7.update()

    #create sub_inner_frame8

    sub_inner_frame8 = tk.Frame(inner_frame)
    sub_inner_frame8.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame8, text='Vitamin D Levels')
    label.pack()

    #create figure, canvas, and toolbar 8
    f8 = figure.Figure(figsize=(5, 5), dpi=100)
    a8 = f8.add_subplot(111)
    a8.plot(creation_date_list(), vd)

    canvas8 = FigureCanvasTkAgg(f8, master=sub_inner_frame8)
    canvas8.draw()
    canvas8.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar8 = NavigationToolbar2Tk(canvas8, sub_inner_frame8)
    toolbar8.update()

    #create sub_inner_frame9

    sub_inner_frame9 = tk.Frame(inner_frame)
    sub_inner_frame9.pack(fill='both', expand=1)

    #create label naming the graph

    label = tk.Label(sub_inner_frame9, text='Total Testosterone Levels')
    label.pack()

    #create figure, canvas, and toolbar 9
    f9 = figure.Figure(figsize=(5, 5), dpi=100)
    a9 = f9.add_subplot(111)
    a9.plot(creation_date_list(), tt)

    canvas9 = FigureCanvasTkAgg(f9, master=sub_inner_frame9)
    canvas9.draw()
    canvas9.get_tk_widget().pack(fill=tk.BOTH, expand=1.0)

    toolbar9 = NavigationToolbar2Tk(canvas9, sub_inner_frame9)
    toolbar9.update()

x = creation_date_list()
wl = get_element_list('health','waist_circumference')
hb = get_element_list('health','hba1c')
hdl = get_element_list('health','hdl')
ldl = get_element_list('health','ldl')
tg = get_element_list('health','triglycerides')
fg = get_element_list('health','fasting_glucose')
fi = get_element_list('health','fasting_insulin')
vd = get_element_list('health','vitamin_d')
tt = get_element_list('health','total_testosterone')


health_graphs(x, wl, hb, hdl, ldl, tg, fg, fi, vd, tt)
inner_frame.after(30000, updateif)

# Subtabs for Frame 3

subtabs3 = ttk.Notebook(third_frame, style='lefttab.TNotebook')
subtabs3.pack(fill="both", expand=1)

subtabs3_frame1 = Frame(subtabs3)
subtabs3_frame1.pack(fill="both", expand=1)
subtabs3_frame2 = Frame(subtabs3)
subtabs3_frame2.pack(fill="both", expand=1)

subtabs3.add(subtabs3_frame1, text="Current")
subtabs3.add(subtabs3_frame2, text="Graphs")



#create mainframe

main_framef = tk.Frame(subtabs3_frame2)
main_framef.pack(fill='both', expand=1)

#create frame that expands endlessly
tkcanvasf = tk.Canvas(main_framef)
tkcanvasf.pack(side='left', fill='both', expand=1)

#create scrollbar

my_scrollbarf = ttk.Scrollbar(main_framef, orient='vertical', command=tkcanvasf.yview)
my_scrollbarf.pack(side='right', fill='y')


#configure the canvas 

tkcanvasf.configure(yscrollcommand=my_scrollbarf.set)
tkcanvasf.bind('<Configure>', lambda e: tkcanvasf.configure(scrollregion = tkcanvasf.bbox('all')))

#create inner canvas frame

inner_framef = tk.Frame(tkcanvasf)


def updateiff():

    x = creation_date_list()
    s = get_element_list('fitness', 'hundred_m_sprint')
    mt = get_element_list('fitness', 'marathon')
    dl = get_element_list('fitness', 'deadlift')
    sq = get_element_list('fitness', 'squat')
    bp = get_element_list('fitness', 'bench_press')
    ohp = get_element_list('fitness', 'overhead_press')
    cup = get_element_list('fitness', 'chin_ups')
    dh = get_element_list('fitness', 'dead_hang')
    vo2 = get_element_list('fitness', 'vo2_max')                  
    
    for item in inner_framef.winfo_children():
        item.destroy()
    fitness_graphs(x, s, mt, dl, sq, bp, ohp, cup, dh, vo2)
    inner_framef.after(30000, updateif)


def fitness_graphs(x, s, mt, dl, sq, bp, ohp, cup, dh, vo2):

    #create window in canvas

    tkcanvasf.create_window((0,0), window=inner_framef, anchor='nw')


    #create sub_inner_frame

    sub_inner_framef = tk.Frame(inner_framef)
    sub_inner_framef.pack(fill='both', expand=1)


    #create label naming the graph

    labelf = tk.Label(sub_inner_framef, text='100M Sprint Time')
    labelf.pack()


    #create figure that fills the subframe
    ff = figure.Figure(figsize=(5, 5), dpi=100)
    af = ff.add_subplot(111)
    af.plot(x, s)


    canvasf = FigureCanvasTkAgg(ff, master=sub_inner_framef)
    canvasf.draw()
    canvasf.get_tk_widget().pack()

    toolbarf = NavigationToolbar2Tk(canvasf, sub_inner_framef)
    toolbarf.update()

    #create sub_inner_frame2

    sub_inner_frame2f = tk.Frame(inner_framef)
    sub_inner_frame2f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame2f, text='Marathon Time')
    labelf.pack()

    #create figure, canvas, and toolbar 2
    ff2 = figure.Figure(figsize=(5, 5), dpi=100)
    af2 = ff2.add_subplot(111)
    af2.plot(x, mt)

    canvasf2 = FigureCanvasTkAgg(ff2, master=sub_inner_frame2f)
    canvasf2.draw()
    canvasf2.get_tk_widget().pack()

    toolbarf2 = NavigationToolbar2Tk(canvasf2, sub_inner_frame2f)
    toolbarf2.update()


    #create sub_inner_frame3

    sub_inner_frame3f = tk.Frame(inner_framef)
    sub_inner_frame3f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame3f, text='Deadlift Weight')
    labelf.pack()

    #create figure, canvas, and toolbar 3

    ff3 = figure.Figure(figsize=(5, 5), dpi=100)
    af3 = ff3.add_subplot(111)
    af3.plot(x, dl)

    canvasf3 = FigureCanvasTkAgg(ff3, master=sub_inner_frame3f)
    canvasf3.draw()
    canvasf3.get_tk_widget().pack()

    toolbarf3 = NavigationToolbar2Tk(canvasf3, sub_inner_frame3f)
    toolbarf3.update()

    #create sub_inner_frame4

    sub_inner_frame4f = tk.Frame(inner_framef)
    sub_inner_frame4f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame4f, text='Squat Weight')
    labelf.pack()

    #create figure, canvas, and toolbar 4

    ff4 = figure.Figure(figsize=(5, 5), dpi=100)
    af4 = ff4.add_subplot(111)
    af4.plot(x, sq)

    canvasf4 = FigureCanvasTkAgg(ff4, master=sub_inner_frame4f)
    canvasf4.draw()
    canvasf4.get_tk_widget().pack()

    toolbarf4 = NavigationToolbar2Tk(canvasf4, sub_inner_frame4f)
    toolbarf4.update()

    #create sub_inner_frame5

    sub_inner_frame5f = tk.Frame(inner_framef)
    sub_inner_frame5f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame5f, text='Bench Press Weight')
    labelf.pack()

    #create figure, canvas, and toolbar 5

    ff5 = figure.Figure(figsize=(5, 5), dpi=100)
    af5 = ff5.add_subplot(111)
    af5.plot(x, bp)

    canvasf5 = FigureCanvasTkAgg(ff5, master=sub_inner_frame5f)
    canvasf5.draw()
    canvasf5.get_tk_widget().pack()

    toolbarf5 = NavigationToolbar2Tk(canvasf5, sub_inner_frame5f)
    toolbarf5.update()

    #create sub_inner_frame6

    sub_inner_frame6f = tk.Frame(inner_framef)
    sub_inner_frame6f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame6f, text='Overhead Press Weight')
    labelf.pack()

    #create figure, canvas, and toolbar 6

    ff6 = figure.Figure(figsize=(5, 5), dpi=100)
    af6 = ff6.add_subplot(111)
    af6.plot(x, ohp)

    canvasf6 = FigureCanvasTkAgg(ff6, master=sub_inner_frame6f)
    canvasf6.draw()
    canvasf6.get_tk_widget().pack()

    toolbarf6 = NavigationToolbar2Tk(canvasf6, sub_inner_frame6f)
    toolbarf6.update()

    #create sub_inner_frame7

    sub_inner_frame7f = tk.Frame(inner_framef)
    sub_inner_frame7f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame7f, text='Chin Up Weight')
    labelf.pack()

    #create figure, canvas, and toolbar 7

    ff7 = figure.Figure(figsize=(5, 5), dpi=100)
    af7 = ff7.add_subplot(111)
    af7.plot(x, cup)

    canvasf7 = FigureCanvasTkAgg(ff7, master=sub_inner_frame7f)
    canvasf7.draw()
    canvasf7.get_tk_widget().pack()

    toolbarf7 = NavigationToolbar2Tk(canvasf7, sub_inner_frame7f)
    toolbarf7.update()

    #create sub_inner_frame8

    sub_inner_frame8f = tk.Frame(inner_framef)
    sub_inner_frame8f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame8f, text='Dead Hang Time')
    labelf.pack()

    #create figure, canvas, and toolbar 8

    ff8 = figure.Figure(figsize=(5, 5), dpi=100)
    af8 = ff8.add_subplot(111)
    af8.plot(x, dh)

    canvasf8 = FigureCanvasTkAgg(ff8, master=sub_inner_frame8f)
    canvasf8.draw()
    canvasf8.get_tk_widget().pack()

    toolbarf8 = NavigationToolbar2Tk(canvasf8, sub_inner_frame8f)
    toolbarf8.update()

    #create sub_inner_frame9

    sub_inner_frame9f = tk.Frame(inner_framef)
    sub_inner_frame9f.pack(fill='both', expand=1)

    #create label naming the graph

    labelf = tk.Label(sub_inner_frame9f, text='VO2 Max')
    labelf.pack()

    #create figure, canvas, and toolbar 9

    ff9 = figure.Figure(figsize=(5, 5), dpi=100)
    af9 = ff9.add_subplot(111)
    af9.plot(x, vo2)

    canvasf9 = FigureCanvasTkAgg(ff9, master=sub_inner_frame9f)
    canvasf9.draw()
    canvasf9.get_tk_widget().pack()

    toolbarf9 = NavigationToolbar2Tk(canvasf9, sub_inner_frame9f)
    toolbarf9.update()

s = get_element_list('fitness', 'hundred_m_sprint')
mt = get_element_list('fitness', 'marathon')
dl = get_element_list('fitness', 'deadlift')
sq = get_element_list('fitness', 'squat')
bp = get_element_list('fitness', 'bench_press')
ohp = get_element_list('fitness', 'overhead_press')
cup = get_element_list('fitness', 'chin_ups')
dh = get_element_list('fitness', 'dead_hang')
vo2 = get_element_list('fitness', 'vo2_max')

fitness_graphs(x, s, mt, dl, sq, bp, ohp, cup, dh, vo2)
inner_framef.after(30000, updateiff)





# subtabs for Frame 4

subtabs4 = ttk.Notebook(fourth_frame, style='lefttab.TNotebook')
subtabs4.pack(fill="both", expand=1)

subtabs4_frame1 = Frame(subtabs4)
subtabs4_frame1.pack(fill="both", expand=1)
subtabs4_frame2 = Frame(subtabs4)
subtabs4_frame2.pack(fill="both", expand=1)

subtabs4.add(subtabs4_frame1, text="Current")
subtabs4.add(subtabs4_frame2, text="Graphs")

#create mainframe

main_framefin = tk.Frame(subtabs4_frame2)
main_framefin.pack(fill='both', expand=1)

#create frame that expands endlessly
tkcanvasfin = tk.Canvas(main_framefin)
tkcanvasfin.pack(side='left', fill='both', expand=1)

#create scrollbar

my_scrollbarfin = ttk.Scrollbar(main_framefin, orient='vertical', command=tkcanvasfin.yview)
my_scrollbarfin.pack(side='right', fill='y')

#configure the canvas

tkcanvasfin.configure(yscrollcommand=my_scrollbarfin.set)
tkcanvasfin.bind('<Configure>', lambda e: tkcanvasfin.configure(scrollregion = tkcanvasfin.bbox('all')))

#create inner canvas frame

inner_framefin = tk.Frame(tkcanvasfin)


def updateiffin():
    
    x = creation_date_list()
    sats = get_element_list('finance', 'total_sats_or_btc')
    mi = get_element_list('finance', 'monthly_income')
    me = get_element_list('finance', 'monthly_expenses_as_percentage_of_m_income')
    db = get_element_list('finance', 'debt')
    av = get_element_list('finance', 'assets_value')          
        
    for item in inner_framefin.winfo_children():
        item.destroy()
    finance_graphs(x, sats, mi, me, db, av)
    inner_framefin.after(30000, updateiffin)



def finance_graphs(x, sats, mi, me, db, av):

    #create window in canvas

    tkcanvasfin.create_window((0,0), window=inner_framefin, anchor='nw')

    #create sub_inner_frame

    sub_inner_framefin = tk.Frame(inner_framefin)
    sub_inner_framefin.pack(fill='both', expand=1)

    #create label naming the graph

    labelfin = tk.Label(sub_inner_framefin, text='BTC or Sats Stacked')
    labelfin.pack()

    #create figure that fills the subframe
    ffin = figure.Figure(figsize=(5, 5), dpi=100)
    afin = ffin.add_subplot(111)
    afin.plot(x, sats)

    canvasfin = FigureCanvasTkAgg(ffin, master=sub_inner_framefin)
    canvasfin.draw()
    canvasfin.get_tk_widget().pack()

    toolbarfin = NavigationToolbar2Tk(canvasfin, sub_inner_framefin)
    toolbarfin.update()

    #create sub_inner_frame2

    sub_inner_frame2fin = tk.Frame(inner_framefin)
    sub_inner_frame2fin.pack(fill='both', expand=1)

    #create label naming the graph

    labelfin = tk.Label(sub_inner_frame2fin, text='Monthly Income')
    labelfin.pack()

    #create figure, canvas, and toolbar 2

    ffin2 = figure.Figure(figsize=(5, 5), dpi=100)
    afin2 = ffin2.add_subplot(111)
    afin2.plot(x, mi)

    canvasfin2 = FigureCanvasTkAgg(ffin2, master=sub_inner_frame2fin)
    canvasfin2.draw()
    canvasfin2.get_tk_widget().pack()

    toolbarfin2 = NavigationToolbar2Tk(canvasfin2, sub_inner_frame2fin)
    toolbarfin2.update()

    #create sub_inner_frame3

    sub_inner_frame3fin = tk.Frame(inner_framefin)
    sub_inner_frame3fin.pack(fill='both', expand=1)

    #create label naming the graph

    labelfin = tk.Label(sub_inner_frame3fin, text='Monthly Expenses As Percentage of Income')
    labelfin.pack()


    #create figure, canvas, and toolbar 3

    ffin3 = figure.Figure(figsize=(5, 5), dpi=100)
    afin3 = ffin3.add_subplot(111)
    afin3.plot(x, me)

    canvasfin3 = FigureCanvasTkAgg(ffin3, master=sub_inner_frame3fin)
    canvasfin3.draw()
    canvasfin3.get_tk_widget().pack()

    toolbarfin3 = NavigationToolbar2Tk(canvasfin3, sub_inner_frame3fin)
    toolbarfin3.update()

    #create sub_inner_frame4

    sub_inner_frame4fin = tk.Frame(inner_framefin)
    sub_inner_frame4fin.pack(fill='both', expand=1)

    #create label naming the graph

    labelfin = tk.Label(sub_inner_frame4fin, text='Debt')
    labelfin.pack()

    #create figure, canvas, and toolbar 4

    ffin4 = figure.Figure(figsize=(5, 5), dpi=100)
    afin4 = ffin4.add_subplot(111)
    afin4.plot(x, db)

    canvasfin4 = FigureCanvasTkAgg(ffin4, master=sub_inner_frame4fin)
    canvasfin4.draw()
    canvasfin4.get_tk_widget().pack()

    toolbarfin4 = NavigationToolbar2Tk(canvasfin4, sub_inner_frame4fin)
    toolbarfin4.update()

    #create sub_inner_frame5

    sub_inner_frame5fin = tk.Frame(inner_framefin)
    sub_inner_frame5fin.pack(fill='both', expand=1)

    #create label naming the graph

    labelfin = tk.Label(sub_inner_frame5fin, text='Assets Value')
    labelfin.pack()

    #create figure, canvas, and toolbar 5

    ffin5 = figure.Figure(figsize=(5, 5), dpi=100)
    afin5 = ffin5.add_subplot(111)
    afin5.plot(x, av)

    canvasfin5 = FigureCanvasTkAgg(ffin5, master=sub_inner_frame5fin)
    canvasfin5.draw()
    canvasfin5.get_tk_widget().pack()

    toolbarfin5 = NavigationToolbar2Tk(canvasfin5, sub_inner_frame5fin)
    toolbarfin5.update()

sats = get_element_list('finance', 'total_sats_or_btc')
mi = get_element_list('finance', 'monthly_income')
me = get_element_list('finance', 'monthly_expenses_as_percentage_of_m_income')
db = get_element_list('finance', 'debt')
av = get_element_list('finance', 'assets_value')


finance_graphs(x, sats, mi, me, db, av)
inner_framefin.after(30000, updateiffin)




#User tab labels and buttons

user_name_label = Label(first_frame, text="Name: "+"{val}".format(val=gather_user_data()[0]))
user_name_label.pack(padx=8, pady=8)

user_age_label = Label(first_frame, text="Age: "+"{val}".format(val= gather_user_data()[1]))
user_age_label.pack(padx=8, pady=8)

user_sex_label = Label(first_frame, text="Sex: "+"{val}".format(val= gather_user_data()[2]))
user_sex_label.pack(padx=8, pady=8)

user_height_label = Label(first_frame, text="Height: "+"{val}".format(val=gather_user_data()[3]))
user_height_label.pack(padx=8, pady=8)


update_user_data = Button(first_frame, text="Update user data", command=update_user_data)
update_user_data.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

#widgets on the health tab


waist_circ_label = Label(subtabs2_frame1, text="Waist Circumference: "+"{val}".format(val=(gather_health_data()[0])))
waist_circ_label.pack()

hba1c_label = Label(subtabs2_frame1, text="HbA1c: "+"{val}".format(val=(gather_health_data()[1])))
hba1c_label.pack()

hdl_label = Label(subtabs2_frame1, text="HDL: "+"{val}".format(val=(gather_health_data()[2])))
hdl_label.pack()

ldl_label = Label(subtabs2_frame1, text="LDL: "+"{val}".format(val=(gather_health_data()[3])))
ldl_label.pack()

tg_label = Label(subtabs2_frame1, text="Triglycerides: "+"{val}".format(val=(gather_health_data()[4])))
tg_label.pack()

fglucose_label = Label(subtabs2_frame1, text="Fasting Glucose: "+"{val}".format(val=(gather_health_data()[5])))
fglucose_label.pack()

finsulin_label = Label(subtabs2_frame1, text="Fasting Insulin: "+"{val}".format(val=(gather_health_data()[6])))
finsulin_label.pack()

vitd_label = Label(subtabs2_frame1, text="Vitamin D: "+"{val}".format(val=(gather_health_data()[7])))
vitd_label.pack()

totalt_label = Label(subtabs2_frame1, text="Total Testosterone: "+"{val}".format(val=(gather_health_data()[8])))
totalt_label.pack()

update_health_data_btn = Button(subtabs2_frame1, text="Update Health Data", command=update_health_data)
update_health_data_btn.pack(side=BOTTOM, anchor="e", padx=8, pady=8)


#widgets on the fitness tab

hundred_m_sprint_label = Label(subtabs3_frame1, text="100m Sprint: "+"{val}".format(val=(gather_fitness_data()[0])))
hundred_m_sprint_label.pack()

marathon_label = Label(subtabs3_frame1, text="Marathon: "+"{val}".format(val=(gather_fitness_data()[1])))
marathon_label.pack()

deadlift_label = Label(subtabs3_frame1, text="Deadlift: "+"{val}".format(val=(gather_fitness_data()[2])))
deadlift_label.pack()

squat_label = Label(subtabs3_frame1, text="Squat: "+"{val}".format(val=(gather_fitness_data()[3])))
squat_label.pack()

bench_press_label = Label(subtabs3_frame1, text="Bench Press: "+"{val}".format(val=(gather_fitness_data()[4])))
bench_press_label.pack()

overhead_press_label = Label(subtabs3_frame1, text="Overhead Press: "+"{val}".format(val=(gather_fitness_data()[5])))
overhead_press_label.pack()

chin_up_label = Label(subtabs3_frame1, text="Chin Up: "+"{val}".format(val=(gather_fitness_data()[6])))
chin_up_label.pack()

dead_hang_label = Label(subtabs3_frame1, text="Dead Hang: "+"{val}".format(val=(gather_fitness_data()[7])))
dead_hang_label.pack()

vo2_label = Label(subtabs3_frame1, text="VO2 Max: "+"{val}".format(val=(gather_fitness_data()[8])))
vo2_label.pack()

update_fitness_data_btn = Button(subtabs3_frame1, text="Update Fitness Data", command=update_fitness_data)
update_fitness_data_btn.pack(side=BOTTOM, anchor="e", padx=8, pady=8)



#widgets on the finance tab

total_sats_or_btc_label = Label(subtabs4_frame1, text="Total Sats: "+"{val}".format(val=(gather_finance_data()[0])))
total_sats_or_btc_label.pack()

monthly_income_label = Label(subtabs4_frame1, text="Monthly Income: "+"{val}".format(val=(gather_finance_data()[1])))
monthly_income_label.pack()

monthly_expenses_label = Label(subtabs4_frame1, text="Monthly Expenses As % Of Income: "+"{val}".format(val=(gather_finance_data()[2])))
monthly_expenses_label.pack()

debt_label = Label(subtabs4_frame1, text="Debt: "+"{val}".format(val=(gather_finance_data()[3])))
debt_label.pack()

assets_value_label = Label(subtabs4_frame1, text="Assets Value: "+"{val}".format(val=(gather_finance_data()[4])))
assets_value_label.pack()

update_finance_data_btn = Button(subtabs4_frame1, text="Update Finance Data", command=update_finance_data)
update_finance_data_btn.pack(side=BOTTOM, anchor="e", padx=8, pady=8)


mainroot.after(1000, update)
mainroot.mainloop()
