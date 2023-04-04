import pandas as pd
from prompt_toolkit.key_binding.bindings import focus

import Attendant_log
import Employees
import os
from datetime import datetime
import csv
import pandas as pd
from datetime import datetime
import Employees

"""
def menu():
    print("Welcome to the Employee database\n")
    print("-1. Add a new empty file\n")
    print("1. Add a new employee\n")
    print("2. add by path existing employees\n")
    print("3. delete employees by id from file you choose\n")
    print("4. Search and display the details for a particular employee in file you choose\n")
    print("5. delete file by path\n")
    print("6. show all employees from file you choose\n")
    print("7. deleting employees from file\n")
    print("0. Quit\n")

    choice = int(input("Please select an option using the numbers above\n"))
    if choice == -1:
        Employees.open_file()
    if choice == 0:
        return
    # if choice == 1:

    #   path = input("Enter file name:")

    #  if os.stat(path).st_size == 0:
    #    Employees.addemployee(str(path))
    # else:
    #   Employees.addemployee_ifnotempty(str(path))
    if choice == 2:
        path = input("Add employees from path:")
        Employees.addemployeebypath(path)
    if choice == 3:
        id_todelete = int(input("enter employee id:"))
        Employees.removemployee(id_todelete)
    if choice == 4:
        id = (input("enter employee id:"))
        Employees.searchemployee(id)
    if choice == 5:
        path = input("deleting file name you cant revert this:")
        Employees.deletemployees(path)
    if choice == 6:
        Employees.showallemployees()
    if choice == 7:
        path = input("deleting employees from path:")
        Employees.deletebypath(path)


def start():
    print("Welcome to TimeTracker\n")
    choice = int(input("Please select an option [1] for employee data base [2] for attendance menu\n"))
    if choice == 1:
        menu()
    if choice == 2:
        Attendance_menu()


def Attendance_menu():
    print("1.Mark Attendance\n")
    print("2.Generate Attendance report of an employee\n")
    print("3.print report for all active employees in last month\n")
    print("4.print an attendance report of all employees who were late(came after 9:30am)\n")
    choice = int(input("Please select an option using the numbers above\n"))
    if choice == 1:
        Attendant_log.markAttendance()

    if choice == 2:
        Attendant_log.report_emp()
    if choice == 3:
        Attendant_log.printall()
    if choice == 4:
        Attendant_log.wholate()
    if choice == 0:
        start()


start()
#start==test

"""

import pandas as df
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import Employees
from tkinter import *
from functools import partial


#######secondary window

def open_secondary_window():
    def delete_data():
        id = emp_id.get()
        Employees.removemployee(id)

    def add_data():
        path = file_path.get()
        Employees.addemployeebypath(path)

    def delete_employee_bypath():
        path = path_.get()
        Employees.deletebypath(path)

    def generate_attendance():
        # Import the tcl file


        # Set the theme with the theme_use method

        data_window = Toplevel()
        #data_window.configure(bg='#333333')
        #data_window.tk.call('source', 'forest-dark.tcl')

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')
        data_window.title("Attendance report")
        id1 = id_1.get()
        df = Employees.searchemployee(int(id1), 'Attendance_file.csv')
        # print(df)
        cols = list(df.columns)

        tree = ttk.Treeview(data_window)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def search():
        data_window = tk.Toplevel()
        #data_window.tk.call('source', 'forest-dark.tcl')

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')
        #data_window.configure(bg='#333333')
        data_window.title("Attendance report")
        id = emp__id.get()
        df = Employees.searchemployee(int(id), 'database.csv')
        cols = list(df.columns)

        tree = ttk.Treeview(data_window)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def report_currentmonth():
        data_window = tk.Toplevel()
        #data_window.configure(bg='#333333')
       # data_window.tk.call('source', 'forest-dark.tcl')

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')
        data_window.title("Attendance report")
        # id = id_.get()
        df = Attendant_log.wholate()
        # print(df)
        cols = list(df.columns)

        tree = ttk.Treeview(data_window)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def attendance_ofall():
        data_window = tk.Toplevel()
        # Import the tcl file
       # data_window.tk.call('source', 'forest-dark.tcl')

        # Set the theme with the theme_use method
        ttk.Style().theme_use('forest-dark')
        #data_window.configure(bg='#333333')
        data_window.title("Attendance report")
        # id = id_.get()
        df = Attendant_log.printall()
        cols = list(df.columns)

        tree = ttk.Treeview(data_window)
        tree.pack()
        tree["columns"] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')

        for index, row in df.iterrows():
            tree.insert("", 0, text=index, values=list(row))

    def enter_data():
        # accepted = accept_var.get()

        # if accepted == "Accepted":
        # User info
        id = first_name_entry.get()
        name = last_name_entry.get()

        if id and name:
            # title = title_combobox.get()
            age = age_spinbox.get()
            # nationality = nationality_combobox.get()

            # Course info
            phone = rphone.get()
            # numcourses = numcourses_spinbox.get()
            # numsemesters = numsemesters_spinbox.get()
            Employees.addemployee_ifnotempty(id, name, phone, age)
            tkinter.messagebox.showwarning(title="Success", message="Data appended successfully")



        else:
            tkinter.messagebox.showwarning(title="Error", message=" name and id are required.")

    # else:
    # tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

    # Create secondary (or popup) window.
    secondary_window = Toplevel()
    #secondary_window.configure(bg='#333333')
    # Import the tcl file
    #secondary_window.tk.call('source', 'forest-dark.tcl')

    # Set the theme with the theme_use method
    ttk.Style().theme_use('forest-dark')
    secondary_window.title("Employee traker")

    frame_1 = tkinter.Frame(secondary_window)
    frame_1.pack()
    #frame_1.configure(bg='#333333')
    user_info_frame = ttk.LabelFrame(frame_1, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)
    #user_info_frame.configure(bg="#333333")
    first_name_label = ttk.Label(user_info_frame, text="Id:")
    first_name_label.grid(row=0, column=0)
    last_name_label = ttk.Label(user_info_frame, text="Name:")
    last_name_label.grid(row=0, column=1)
    rphone = ttk.Label(user_info_frame, text="phone:")
    rphone.grid(row=0, column=2)

    first_name_entry = ttk.Entry(user_info_frame)
    last_name_entry = ttk.Entry(user_info_frame)
    rphone = ttk.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)
    rphone.grid(row=1, column=2)
    """
     title_label = tkinter.Label(user_info_frame, text="Title")
     title_combobox = ttk.Combobox(user_info_frame, values=["", "Manager", "Senior", "Junior"])
     title_label.grid(row=0, column=3)
     title_combobox.grid(row=1, column=3)
    """
    age_label = ttk.Label(user_info_frame, text="Age:")
    age_spinbox =ttk.Spinbox(user_info_frame, from_=18, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    # nationality_label = tkinter.Label(user_info_frame, text="Nationality")
    # nationality_combobox = ttk.Combobox(user_info_frame,
    #                                   values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania",
    #                                          "South America"])
    # nationality_label.grid(row=2, column=1)
    # nationality_combobox.grid(row=3, column=1)

    # Button to enter data
    button = ttk.Button(user_info_frame, text="Add new Employee", command=enter_data)
    button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
    button = ttk.Button(user_info_frame, text="Show all Employees", command=Employees.showallemployees)
    button.grid(row=4, column=2, sticky="news", padx=20, pady=10)

    first_name_entry.delete(0, "end")
    last_name_entry.delete(0, "end")
    rphone.delete(0, "end")
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    ##########################################################################################################
    addemployee_from_file = ttk.LabelFrame(frame_1, text="Add Employee by path")
    addemployee_from_file.grid(row=1, column=0, padx=20, pady=10)
    #addemployee_from_file.configure(bg="#333333")
    file_path = ttk.Label(addemployee_from_file, text="file path:")
    file_path.grid(row=0, column=0)
    file_path = ttk.Entry(addemployee_from_file)
    file_path.grid(row=0, column=1)
    button_file = ttk.Button(addemployee_from_file, text="Add new Employees", command=add_data)
    button_file.grid(row=3, column=1)
    file_path.delete(0, "end")
    for widget in addemployee_from_file.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    ##########################################################################################################
    delete_from_file = ttk.LabelFrame(frame_1, text="Delete employee by id")
    delete_from_file.grid(row=1, column=1, padx=20, pady=10)
    #delete_from_file.configure(bg="#333333")
    emp_id = ttk.Label(delete_from_file, text="id:")
    emp_id.grid(row=0, column=0)
    emp_id = ttk.Entry(delete_from_file)
    emp_id.grid(row=0, column=1)
    button_file =ttk.Button(delete_from_file, text="delete Employees",
                                 command=delete_data)
    button_file.grid(row=0, column=2)
    emp__id = ttk.Label(delete_from_file, text="search id:")
    emp__id.grid(row=1, column=0)
    emp__id = ttk.Entry(delete_from_file)
    emp__id.grid(row=1, column=1)

    button_file1 =ttk.Button(delete_from_file, text="search Employees",
                                  command=search)

    button_file1.grid(row=1, column=2)
    emp__id.delete(0, "end")
    emp_id.delete(0, "end")
    for widget in delete_from_file.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    ##########################################################################################################
    path_file =ttk.LabelFrame(frame_1, text="Delete employees by path")
    path_file.grid(row=3, column=0, padx=20, pady=10)
    #path_file.configure(bg="#333333")
    path_ = ttk.Label(path_file, text="path:")
    path_.grid(row=0, column=0)
    path_ = ttk.Entry(path_file)
    path_.grid(row=0, column=2)
    button_file =ttk.Button(path_file, text="add path", command=delete_employee_bypath)
    button_file.grid(row=3, column=1)
    path_.delete(0, "end")


    for widget in path_file.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #######################################################################################################
    gerate_frame =ttk.LabelFrame(frame_1, text="Generate Attendance report of an employee"
                                     )
    gerate_frame.grid(row=3, column=1, padx=20, pady=10)
    #gerate_frame.configure(bg="#333333")
    id_1 = ttk.Label(gerate_frame, text="id:")
    id_1.grid(row=0, column=0)
    id_1 = ttk.Entry(gerate_frame)
    id_1.grid(row=0, column=1)
    button_file_ = ttk.Button(gerate_frame, text="generate", command=generate_attendance)
    button_file_.grid(row=0, column=2)

    button_file1 = ttk.Button(gerate_frame, text="current month who late", command=report_currentmonth)
    button_file1.grid(row=4, column=1)

    button_file2 = ttk.Button(gerate_frame, text="generate all last month", command=attendance_ofall)
    button_file2.grid(row=4, column=2)
    id_1.delete(0, "end")
    for widget in gerate_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


#######################################################################################################
#####main window
def mark():
    id = id_label.get()

    if id:
        Attendant_log.markAttendance(id)


window = tkinter.Tk()
window.title("Welcome to TimeTracker")
#window.configure(bg='#333333')
# Import the tcl file
window.tk.call('source', 'forest-dark.tcl')

# Set the theme with the theme_use method
ttk.Style().theme_use('forest-dark')
frame = tkinter.Frame(window)
frame.pack()
#frame.configure(bg='#333333')

#################################################################################################
# login frame

login_frame = ttk.LabelFrame(frame, text="Login")
#login_frame.configure(bg='#333333')
login_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)


def validateLogin(username, password):
    username_ = "rita"
    password_ = "123456"
    if username.get() == username_ and password.get() == password_:
        print("successfully logged in")
        open_secondary_window()
    else:
        print("wrong password")


# username label and text entry box
usernameLabel = ttk.Label(login_frame, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = ttk.Entry(login_frame, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = ttk.Label(login_frame, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = ttk.Entry(login_frame, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

# login button

button_open = ttk.Button(
    login_frame,
    text="Login to Employee database",
    command=validateLogin
)
button_open.grid(row=3, column=1, sticky="news", padx=20, pady=20)

##############################################################################################################


# Mark Attendance Info
courses_frame = ttk.LabelFrame(frame, text="Mark Attendance")
#courses_frame.configure(bg='#333333')
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20)

"""
registered_label = tkinter.LabelFrame(courses_frame, text="Mark Attendance")
registered_label.grid(row=0, column=0)
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                      variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
"""

id_label = ttk.Label(courses_frame, text="Id:")
id_label.grid(row=2, column=0)
id_label = ttk.Entry(courses_frame)
id_label.grid(row=2, column=1)
button = ttk.Button(courses_frame, text="Mark Attendance")
button.grid(row=3, column=1, sticky="news", padx=20, pady=20)
id_label.delete(0, "end")
"""
numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)
"""
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms

terms_frame = ttk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)
#terms_frame.configure(bg='#333333')
accept_var = StringVar(value="Not Accepted")
terms_check = ttk.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

window.mainloop()
