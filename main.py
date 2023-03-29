import pandas as pd
from prompt_toolkit.key_binding.bindings import focus

import Attendant_log
import Employees
import os
from datetime import datetime
import csv


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


# start()
#start==test






import time
# importing webdriver from selenium
import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os
import openpyxl
import Employees



def open_secondary_window():
    def enter_data():
       # accepted = accept_var.get()

       #if accepted == "Accepted":
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
        #else:
            #tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

    # Create secondary (or popup) window.
    secondary_window = tk.Toplevel()
    secondary_window.title("Employee traker")
    secondary_window.config(width=300, height=200)
    user_info_frame = tkinter.LabelFrame(secondary_window, text="User Information")
    user_info_frame.grid(row=0, column=0, padx=20, pady=10)

    first_name_label = tkinter.Label(user_info_frame, text="Id:")
    first_name_label.grid(row=0, column=0)
    last_name_label = tkinter.Label(user_info_frame, text="Name:")
    last_name_label.grid(row=0, column=1)
    rphone = tkinter.Label(user_info_frame, text="phone:")
    rphone.grid(row=0, column=2)

    first_name_entry = tkinter.Entry(user_info_frame)
    last_name_entry = tkinter.Entry(user_info_frame)
    rphone = tkinter.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)
    rphone.grid(row=1, column=2)

    # title_label = tkinter.Label(user_info_frame, text="Title")
    # title_combobox = ttk.Combobox(user_info_frame, values=["", "Menager", "Senior", "Junior"])
    # title_label.grid(row=0, column=3)
    # title_combobox.grid(row=1, column=3)

    age_label = tkinter.Label(user_info_frame, text="Age:")
    age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
    age_label.grid(row=2, column=0)
    age_spinbox.grid(row=3, column=0)

    # nationality_label = tkinter.Label(user_info_frame, text="Nationality")
    # nationality_combobox = ttk.Combobox(user_info_frame,
    #                                   values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania",
    #                                          "South America"])
    # nationality_label.grid(row=2, column=1)
    # nationality_combobox.grid(row=3, column=1)

    # Button to enter data
    button = tkinter.Button(user_info_frame, text="Add new Employee", command=enter_data)
    button.grid(row=4, column=1, sticky="news", padx=20, pady=10)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        secondary_window,
        text="Close window",
        command=secondary_window.destroy
    )
    button_close.grid(row=4, column=0, sticky="news", padx=20, pady=10)

def mark():
    id = id_label.get()

    if id:
        Attendant_log.markAttendance(id)


window = tkinter.Tk()
window.title("Welcome to TimeTracker")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info


#Mark Attendance Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label= tkinter.Label(courses_frame, text="Mark Attendance")
registered_label.grid(row=1, column=0)
#registered_label = tkinter.LabelFrame(courses_frame, text="Mark Attendance")
#registered_label.grid(row=0, column=0)
#reg_status_var = tkinter.StringVar(value="Not Registered")
#registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                      # variable=reg_status_var, onvalue="Registered", offvalue="Not registered")


id_label = tkinter.Label(courses_frame, text="Id-->")
id_label.grid(row=2, column=0)
id_label = tkinter.Entry(courses_frame)
id_label.grid(row=2, column=1)
button = tkinter.Button(courses_frame, text="Mark Attendance", command=mark)
button.grid(row=3, column=1, sticky="news", padx=20, pady=10)

#numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
#numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
#numcourses_label.grid(row=0, column=1)
#numcourses_spinbox.grid(row=1, column=1)

#numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
#numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
#numsemesters_label.grid(row=0, column=2)
#numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms

terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

button_open = ttk.Button(
    frame,
    text="Employee database",
    command=open_secondary_window
)
button_open.grid(row=0, column=0, sticky="news", padx=20, pady=10)


window.mainloop()
