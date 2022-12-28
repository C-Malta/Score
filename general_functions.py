import tkinter as tk
import random
import xml.etree.ElementTree as ET
import os
import re
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import time
import subprocess




def get_last_file():
    
    list = ""

    for file in os.listdir():
        if re.match('Data', file):
            list = list + " " + file

    splitlist = list.split(" ")
    latest_file = splitlist[-1]
    return latest_file

def get_splitlist():
    list = ""
    for file in os.listdir():
        if re.match('Data', file):
            list = list + " " + file
            splitlist = list.split(" ")
    return splitlist



def creation_date_list():
    def get_file_creation_date_converted(path):

        date = datetime.fromtimestamp(os.path.getctime(path))
        date = str(date)
        date = date.split()
        date = date[0]
        date = date.split('-')
        date = date[0] + ', ' + date[1] + ', ' + date[2]
        return date


    splitlist = get_splitlist()
    file_creation_dates_converted = []
    for item in splitlist:
        if item != splitlist[0]:
            file_creation_dates_converted.append(get_file_creation_date_converted(item))
    return file_creation_dates_converted
            


def get_element_list(section, lelement):

    splitlist = get_splitlist()

    def gather_elements(file):
        tree = ET.parse(file)
        treeroot = tree.getroot()

        for element in treeroot.findall(section):
            elements = element.find(lelement).text

        return float(elements)

    element_list = []
    for item in splitlist:
        if item != splitlist[0]:
            element_list.append(gather_elements(item))
    return element_list

def delete_data(file, section):

    tree = ET.parse(file)
    treeroot = tree.getroot()

    for element in treeroot.findall(section):
        treeroot.remove(element)

    tree.write(file)


def createfile():
    
    latest_file = get_last_file()
    latest_file_name = (latest_file.split("."))[0]

    file_number = ""
    for c in latest_file_name:
        if c.isdigit():
            file_number = file_number + c

       
    name = gather_user_data()[0]
    age = gather_user_data()[1]
    sex = gather_user_data()[2]
    height = gather_user_data()[3]

    waist_circumference = gather_health_data()[0]
    hba1c = gather_health_data()[1]
    hdl = gather_health_data()[2]
    ldl = gather_health_data()[3]
    triglycerides = gather_health_data()[4]
    fasting_glucose = gather_health_data()[5]
    fasting_insulin = gather_health_data()[6]
    vitamin_d = gather_health_data()[7]
    total_testosterone = gather_health_data()[8]

    hundred_m_sprint = gather_fitness_data()[0]
    marathon = gather_fitness_data()[1]
    deadlift = gather_fitness_data()[2]
    squat = gather_fitness_data()[3]
    bench_press = gather_fitness_data()[4]
    overhead_press = gather_fitness_data()[5]
    chin_ups = gather_fitness_data()[6]
    dead_hang = gather_fitness_data()[7]
    vo2_max = gather_fitness_data()[8]

    total_sats_or_btc = gather_finance_data()[0]
    monthly_income = gather_finance_data()[1]
    monthly_expenses_as_percentage_of_m_income = gather_finance_data()[2]
    debt = gather_finance_data()[3]
    assets_value = gather_finance_data()[4]
            
    next_file_number = int(file_number) + 1
    user_file_name = "Data" + str(next_file_number)
    f = open("{val}.xml".format(val=user_file_name), "x")
    f.flush()
    os.fsync(f.fileno())
    f.write('<root><user><name>' + name + '</name><age>' + age + '</age><sex>' + sex + '</sex><height>' + height + '</height></user><health><waist_circumference>' + waist_circumference + '</waist_circumference><hba1c>' + hba1c + '</hba1c><hdl>' + hdl + '</hdl><ldl>' + ldl + '</ldl><triglycerides>' + triglycerides + '</triglycerides><fasting_glucose>' + fasting_glucose + '</fasting_glucose><fasting_insulin>' + fasting_insulin + '</fasting_insulin><vitamin_d>' + vitamin_d + '</vitamin_d><total_testosterone>' + total_testosterone + '</total_testosterone></health><fitness><hundred_m_sprint>' + hundred_m_sprint + '</hundred_m_sprint><marathon>' + marathon + '</marathon><deadlift>' + deadlift + '</deadlift><squat>' + squat + '</squat><bench_press>' + bench_press + '</bench_press><overhead_press>' + overhead_press + '</overhead_press><chin_ups>' + chin_ups + '</chin_ups><dead_hang>' + dead_hang + '</dead_hang><vo2_max>' + vo2_max + '</vo2_max></fitness><finance><total_sats_or_btc>' + total_sats_or_btc + '</total_sats_or_btc><monthly_income>' + monthly_income + '</monthly_income><monthly_expenses_as_percentage_of_m_income>' + monthly_expenses_as_percentage_of_m_income + '</monthly_expenses_as_percentage_of_m_income><debt>' + debt + '</debt><assets_value>' + assets_value + '</assets_value></finance></root>')
    return user_file_name+".xml"


def gather_user_data():

  
    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()


    for user in treeroot.findall('user'):
        username = user.find('name').text
        userage = user.find('age').text
        usersex = user.find('sex').text
        userheight = user.find('height').text

    misc_data = [username, userage, usersex, userheight]
    return misc_data


#create function to gather health data

def gather_health_data():

    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for health in treeroot.findall('health'):
        waist_circ = health.find('waist_circumference').text
        hba1c = health.find('hba1c').text
        hdl = health.find('hdl').text
        ldl = health.find('ldl').text
        triglycerides = health.find('triglycerides').text
        fasting_glucose = health.find('fasting_glucose').text
        fasting_insulin = health.find('fasting_insulin').text
        vitamin_d = health.find('vitamin_d').text
        total_testosterone = health.find('total_testosterone').text

    health_data = [waist_circ,hba1c,hdl,ldl,triglycerides,fasting_glucose,fasting_insulin,vitamin_d,total_testosterone]
    return health_data

#create function to gather fitness data

def gather_fitness_data():

 

    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for fitness in treeroot.findall('fitness'):
        hundred_m_sprint = fitness.find('hundred_m_sprint').text
        marathon = fitness.find('marathon').text
        deadlift = fitness.find('deadlift').text
        squat = fitness.find('squat').text
        bench_press = fitness.find('bench_press').text
        overhead_press = fitness.find('overhead_press').text
        chin_ups = fitness.find('chin_ups').text
        dead_hang = fitness.find('dead_hang').text
        vo2_max = fitness.find('vo2_max').text

    fitness_data = [hundred_m_sprint,marathon,deadlift,squat,bench_press,overhead_press,chin_ups,dead_hang,vo2_max]
    return fitness_data



def gather_finance_data():


    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for finance in treeroot.findall('finance'):
        total_sats_or_btc = finance.find('total_sats_or_btc').text
        monthly_income = finance.find('monthly_income').text
        monthly_expenses_as_percentage_of_m_income = finance.find('monthly_expenses_as_percentage_of_m_income').text
        debt = finance.find('debt').text
        assets_value = finance.find('assets_value').text

    finance_data = [total_sats_or_btc, monthly_income, monthly_expenses_as_percentage_of_m_income, debt, assets_value]
    return finance_data






def write_user_data(file, name, age, sex, height):

    tree = ET.parse(file)

    userdata = ET.fromstring("<user><name>"+name+"</name><age>"+age+"</age><sex>"+sex+"</sex><height>"+height+"</height></user>")
    root = tree.getroot()
    root.append(userdata)

    tree.write(file)


def write_health_data(file, waist_circumference, hba1c, hdl, ldl, triglycerides, fasting_glucose, fasting_insulin, vitamin_d, total_testosterone):
    


    tree = ET.parse(file)


    healthdata = ET.fromstring("<health><waist_circumference>"+str(waist_circumference)+"</waist_circumference><hba1c>"+str(hba1c)+"</hba1c><hdl>"+str(hdl)+"</hdl><ldl>"+str(ldl)+"</ldl><triglycerides>"+str(triglycerides)+"</triglycerides><fasting_glucose>"+str(fasting_glucose)+"</fasting_glucose><fasting_insulin>"+str(fasting_insulin)+"</fasting_insulin><vitamin_d>"+str(vitamin_d)+"</vitamin_d><total_testosterone>"+str(total_testosterone)+"</total_testosterone></health>")
    root = tree.getroot()
    root.append(healthdata)

    tree.write(file)


   
def write_fitness_data(file, hundred_m_sprint, marathon, deadlift, squat, bench_press, overhead_press, chin_ups, dead_hang, vo2_max):
   
    tree = ET.parse(file)
    root = tree.getroot()

    fitnessdata = ET.fromstring("<fitness><hundred_m_sprint>"+str(hundred_m_sprint)+"</hundred_m_sprint><marathon>"+str(marathon)+"</marathon><deadlift>"+str(deadlift)+"</deadlift><squat>"+str(squat)+"</squat><bench_press>"+str(bench_press)+"</bench_press><overhead_press>"+str(overhead_press)+"</overhead_press><chin_ups>"+str(chin_ups)+"</chin_ups><dead_hang>"+str(dead_hang)+"</dead_hang><vo2_max>"+str(vo2_max)+"</vo2_max></fitness>")
    root.append(fitnessdata)

    tree.write(file)

def write_finance_data(file, total_sats_or_btc, monthly_income, monthly_expenses_as_percentage_of_m_income, debt, assets_value):
  
    tree = ET.parse(file)
    root = tree.getroot()

    finance_data = ET.fromstring("<finance><total_sats_or_btc>"+str(total_sats_or_btc)+"</total_sats_or_btc><monthly_income>"+str(monthly_income)+"</monthly_income><monthly_expenses_as_percentage_of_m_income>"+str(monthly_expenses_as_percentage_of_m_income)+"</monthly_expenses_as_percentage_of_m_income><debt>"+str(debt)+"</debt><assets_value>"+str(assets_value)+"</assets_value></finance>")
    root.append(finance_data)

    tree.write(file)


def gather_user_data():

  
    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()


    for user in treeroot.findall('user'):
        username = user.find('name').text
        userage = user.find('age').text
        usersex = user.find('sex').text
        userheight = user.find('height').text

    misc_data = [username, userage, usersex, userheight]
    return misc_data




#create function to gather health data

def gather_health_data():

    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for health in treeroot.findall('health'):
        waist_circ = health.find('waist_circumference').text
        hba1c = health.find('hba1c').text
        hdl = health.find('hdl').text
        ldl = health.find('ldl').text
        triglycerides = health.find('triglycerides').text
        fasting_glucose = health.find('fasting_glucose').text
        fasting_insulin = health.find('fasting_insulin').text
        vitamin_d = health.find('vitamin_d').text
        total_testosterone = health.find('total_testosterone').text

    health_data = [waist_circ,hba1c,hdl,ldl,triglycerides,fasting_glucose,fasting_insulin,vitamin_d,total_testosterone]
    return health_data

#create function to gather fitness data

def gather_fitness_data():

 

    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for fitness in treeroot.findall('fitness'):
        hundred_m_sprint = fitness.find('hundred_m_sprint').text
        marathon = fitness.find('marathon').text
        deadlift = fitness.find('deadlift').text
        squat = fitness.find('squat').text
        bench_press = fitness.find('bench_press').text
        overhead_press = fitness.find('overhead_press').text
        chin_ups = fitness.find('chin_ups').text
        dead_hang = fitness.find('dead_hang').text
        vo2_max = fitness.find('vo2_max').text

    fitness_data = [hundred_m_sprint,marathon,deadlift,squat,bench_press,overhead_press,chin_ups,dead_hang,vo2_max]
    return fitness_data



def gather_finance_data():


    tree = ET.parse(get_last_file())
    treeroot = tree.getroot()

    for finance in treeroot.findall('finance'):
        total_sats_or_btc = finance.find('total_sats_or_btc').text
        monthly_income = finance.find('monthly_income').text
        monthly_expenses_as_percentage_of_m_income = finance.find('monthly_expenses_as_percentage_of_m_income').text
        debt = finance.find('debt').text
        assets_value = finance.find('assets_value').text

    finance_data = [total_sats_or_btc, monthly_income, monthly_expenses_as_percentage_of_m_income, debt, assets_value]
    return finance_data


def update_user_data():
    def submit_misc_data():
        newf = createfile()
        delete_data(newf, 'user')
        name = name_entry.get()
        age = age_entry.get()
        sex = sex_entry.get()
        height = height_entry.get()
        write_user_data(newf, name, age, sex, height)


    # create the root window
    root = tk.Tk()


    # create a frame to hold the widgets
    frame = tk.Frame(root)

    #button press function

    def button_press():
        submit_misc_data()
        root.destroy()


    # create the widgets
    name_label = tk.Label(frame, text="Name:")
    age_label = tk.Label(frame, text="Age:")
    sex_label = tk.Label(frame, text="Sex:")
    height_label = tk.Label(frame, text="Height:")
    name_entry = tk.Entry(frame)
    name_entry.insert(0, "{val}".format(val=(gather_user_data()[0])))
    age_entry = tk.Entry(frame)
    age_entry.insert(0, "{val}".format(val=(gather_user_data()[1])))
    sex_entry = tk.Entry(frame)
    sex_entry.insert(0, "{val}".format(val=(gather_user_data()[2])))
    height_entry = tk.Entry(frame)
    height_entry.insert(0, "{val}".format(val=(gather_user_data()[3])))
    submit_button = tk.Button(frame, text="Submit", command=button_press)

    # add the widgets to the frame
    name_label.grid(row=0, column=0)
    age_label.grid(row=1, column=0)
    sex_label.grid(row=2, column=0)
    height_label.grid(row=3, column=0)
    name_entry.grid(row=0, column=1)
    age_entry.grid(row=1, column=1)
    sex_entry.grid(row=2, column=1)
    height_entry.grid(row=3, column=1)
    submit_button.grid(row=4, column=1)

    # add the frame to the root window
    frame.pack()

    # run the main loop
    root.mainloop()

def update_health_data():


    def submit_health_data():
        newf = createfile()
        delete_data(newf, 'health')
        waist_circumference = waist_entry.get()
        hba1c = hba1c_entry.get()
        hdl = hdl_entry.get()
        ldl = ldl_entry.get()
        triglycerides = triglycerides_entry.get()
        fasting_glucose = glucose_entry.get()
        fasting_insulin = insulin_entry.get()
        vitamin_d = vitamin_entry.get()
        total_testosterone = testosterone_entry.get()
        write_health_data(newf, waist_circumference, hba1c, hdl, ldl, triglycerides, fasting_glucose, fasting_insulin, vitamin_d,total_testosterone)

    #button press function

    def button_press():
        submit_health_data()
        root.destroy()


    # create the root window

    root = tk.Tk()




    # create a frame to hold the widgets
    frame = tk.Frame(root)


    waist_label = tk.Label(frame, text="Waist Circumference:")
    hba1c_label = tk.Label(frame, text="HbA1c:")
    hdl_label = tk.Label(frame, text="HDL:")
    ldl_label = tk.Label(frame, text="LDL:")
    triglycerides_label = tk.Label(frame, text="Triglycerides:")
    glucose_label = tk.Label(frame, text="Fasting Glucose:")
    insulin_label = tk.Label(frame, text="Fasting Insulin:")
    vitamin_label = tk.Label(frame, text="Vitamin D:")
    testosterone_label = tk.Label(frame, text="Total Testosterone:")
    waist_entry = tk.Entry(frame)
    waist_entry.insert(0, "{val}".format(val=(gather_health_data()[0])))
    hba1c_entry = tk.Entry(frame)
    hba1c_entry.insert(0, "{val}".format(val=(gather_health_data()[1])))
    hdl_entry = tk.Entry(frame)
    hdl_entry.insert(0, "{val}".format(val=(gather_health_data()[2])))
    ldl_entry = tk.Entry(frame)
    ldl_entry.insert(0, "{val}".format(val=(gather_health_data()[3])))
    triglycerides_entry = tk.Entry(frame)
    triglycerides_entry.insert(0, "{val}".format(val=(gather_health_data()[4])))
    glucose_entry = tk.Entry(frame)
    glucose_entry.insert(0, "{val}".format(val=(gather_health_data()[5])))
    insulin_entry = tk.Entry(frame)
    insulin_entry.insert(0, "{val}".format(val=(gather_health_data()[6])))
    vitamin_entry = tk.Entry(frame)
    vitamin_entry.insert(0, "{val}".format(val=(gather_health_data()[7])))
    testosterone_entry = tk.Entry(frame)
    testosterone_entry.insert(0, "{val}".format(val=(gather_health_data()[8])))
    submit_button = tk.Button(frame, text="Submit", command=button_press)

    # Add the widgets to the frame
    waist_label.grid(row=0, column=0)
    hba1c_label.grid(row=1, column=0)
    hdl_label.grid(row=2, column=0)
    ldl_label.grid(row=3, column=0)
    triglycerides_label.grid(row=4, column=0)
    glucose_label.grid(row=5, column=0)
    insulin_label.grid(row=6, column=0)
    vitamin_label.grid(row=7, column=0)
    testosterone_label.grid(row=8, column=0)
    waist_entry.grid(row=0, column=1)
    hba1c_entry.grid(row=1, column=1)
    hdl_entry.grid(row=2, column=1)
    ldl_entry.grid(row=3, column=1)
    triglycerides_entry.grid(row=4, column=1)
    glucose_entry.grid(row=5, column=1)
    insulin_entry.grid(row=6, column=1)
    vitamin_entry.grid(row=7, column=1)
    testosterone_entry.grid(row=8, column=1)
    submit_button.grid(row=9, column=1)

    # Add the frame to the root window
    frame.pack()

    # run the main loop
    root.mainloop()

def update_fitness_data():
    def submit_fitness_data():
        newf = createfile()
        delete_data(newf, 'fitness')
        hundred_m_sprint = hundred_m_sprint_entry.get()
        marathon = marathon_entry.get()
        deadlift = deadlift_entry.get()
        squat = squat_entry.get()
        bench_press = bench_press_entry.get()
        overhead_press = overhead_press_entry.get()
        chin_ups = chin_ups_entry.get()
        dead_hang = dead_hang_entry.get()
        vo2_max = vo2_max_entry.get()
        write_fitness_data(newf, hundred_m_sprint, marathon, deadlift, squat, bench_press, overhead_press, chin_ups, dead_hang, vo2_max)

    # create the root window
    root = tk.Tk()

    # create a frame to hold the widgets
    frame = tk.Frame(root)

    #button press function

    def button_press():
        submit_fitness_data()
        root.destroy()

    # create the widgets
    hundred_m_sprint_label = tk.Label(frame, text="100m Sprint:")
    marathon_label = tk.Label(frame, text="Marathon:")
    deadlift_label = tk.Label(frame, text="Deadlift:")
    squat_label = tk.Label(frame, text="Squat:")
    bench_press_label = tk.Label(frame, text="Bench Press:")
    overhead_press_label = tk.Label(frame, text="Overhead Press:")
    chin_ups_label = tk.Label(frame, text="Chin-ups:")
    dead_hang_label = tk.Label(frame, text="Dead Hang:")
    vo2_max_label = tk.Label(frame, text="VO2 Max:")
    hundred_m_sprint_entry = tk.Entry(frame)
    hundred_m_sprint_entry.insert(0, "{val}".format(val=(gather_fitness_data()[0])))
    marathon_entry = tk.Entry(frame)
    marathon_entry.insert(0, "{val}".format(val=(gather_fitness_data()[1])))
    deadlift_entry = tk.Entry(frame)
    deadlift_entry.insert(0, "{val}".format(val=(gather_fitness_data()[2])))
    squat_entry = tk.Entry(frame)
    squat_entry.insert(0, "{val}".format(val=(gather_fitness_data()[3])))
    bench_press_entry = tk.Entry(frame)
    bench_press_entry.insert(0, "{val}".format(val=(gather_fitness_data()[4])))
    overhead_press_entry = tk.Entry(frame)
    overhead_press_entry.insert(0, "{val}".format(val=(gather_fitness_data()[5])))
    chin_ups_entry = tk.Entry(frame)
    chin_ups_entry.insert(0, "{val}".format(val=(gather_fitness_data()[6])))
    dead_hang_entry = tk.Entry(frame)
    dead_hang_entry.insert(0, "{val}".format(val=(gather_fitness_data()[7])))
    vo2_max_entry = tk.Entry(frame)
    vo2_max_entry.insert(0, "{val}".format(val=(gather_fitness_data()[8])))
    submit_button = tk.Button(frame, text="Submit", command=button_press)

    # Add the widgets to the frame

    hundred_m_sprint_label.grid(row=0, column=0)
    marathon_label.grid(row=1, column=0)
    deadlift_label.grid(row=2, column=0)
    squat_label.grid(row=3, column=0)
    bench_press_label.grid(row=4, column=0)
    overhead_press_label.grid(row=5, column=0)
    chin_ups_label.grid(row=6, column=0)
    dead_hang_label.grid(row=7, column=0)
    vo2_max_label.grid(row=8, column=0)
    hundred_m_sprint_entry.grid(row=0, column=1)
    marathon_entry.grid(row=1, column=1)
    deadlift_entry.grid(row=2, column=1)
    squat_entry.grid(row=3, column=1)
    bench_press_entry.grid(row=4, column=1)
    overhead_press_entry.grid(row=5, column=1)
    chin_ups_entry.grid(row=6, column=1)
    dead_hang_entry.grid(row=7, column=1)
    vo2_max_entry.grid(row=8, column=1)
    submit_button.grid(row=9, column=1)

    # Add the frame to the root window
    frame.pack()

    # run the main loop
    root.mainloop()


def update_finance_data():

    def submit_finance_data():
        newf = createfile()
        delete_data(newf, 'finance')
        total_sats_or_btc = total_sats_or_btc_entry.get()
        monthly_income = monthly_income_entry.get()
        monthly_expenses_as_percentage_of_m_income = monthly_expenses_as_percentage_of_m_income_entry.get()
        debt = debt_entry.get()
        assets_value = assets_value_entry.get()
        write_finance_data(newf, total_sats_or_btc, monthly_income, monthly_expenses_as_percentage_of_m_income, debt, assets_value)

    # create the root window
    root = tk.Tk()

    # create a frame to hold the widgets
    frame = tk.Frame(root)

    #button press function

    def button_press():
        submit_finance_data()
        root.destroy()

    total_sats_or_btc_label = tk.Label(frame, text="Total Sats:")
    monthly_income_label = tk.Label(frame, text="Monthly Income:")
    monthly_expenses_as_percentage_of_m_income_label = tk.Label(frame, text="Monthly Expenses as Percentage of M Income:")
    debt_label = tk.Label(frame, text="Debt:")
    assets_value_label = tk.Label(frame, text="Assets Value:")
    total_sats_or_btc_entry = tk.Entry(frame)
    total_sats_or_btc_entry.insert(0, "{val}".format(val=(gather_finance_data()[0])))
    monthly_income_entry = tk.Entry(frame)
    monthly_income_entry.insert(0, "{val}".format(val=(gather_finance_data()[1])))
    monthly_expenses_as_percentage_of_m_income_entry = tk.Entry(frame)
    monthly_expenses_as_percentage_of_m_income_entry.insert(0, "{val}".format(val=(gather_finance_data()[2])))
    debt_entry = tk.Entry(frame)
    debt_entry.insert(0, "{val}".format(val=(gather_finance_data()[3])))
    assets_value_entry = tk.Entry(frame)
    assets_value_entry.insert(0, "{val}".format(val=(gather_finance_data()[4])))
    submit_button = tk.Button(frame, text="Submit", command=button_press)

    # Add the widgets to the frame

    total_sats_or_btc_label.grid(row=0, column=0)
    monthly_income_label.grid(row=1, column=0)
    monthly_expenses_as_percentage_of_m_income_label.grid(row=2, column=0)
    debt_label.grid(row=3, column=0)
    assets_value_label.grid(row=4, column=0)
    total_sats_or_btc_entry.grid(row=0, column=1)
    monthly_income_entry.grid(row=1, column=1)
    monthly_expenses_as_percentage_of_m_income_entry.grid(row=2, column=1)
    debt_entry.grid(row=3, column=1)
    assets_value_entry.grid(row=4, column=1)
    submit_button.grid(row=5, column=1)

    # Add the frame to the root window
    frame.pack()

    # run the main loop
    root.mainloop()


    
    
