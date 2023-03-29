import csv
import pandas as pd
from datetime import datetime
import Employees


class Attendant_log:

    def __init__(self, employee_id, time, name,date):
        self.employee_id = employee_id
        self.name = name
        self.time = time
        self.date=date



#report of all employees in the attandce file

def report_emp():
    print("Adding a new attendance, please enter the following details\n")
    _id = int(input("Enter your employee ID\n"))
    print("you need to enter file name Attendance_file.csv\n")
    Employees.searchemployee(_id)


#print all employees attendance in last month
def printall():
    now_date = datetime.now()
    date = now_date.strftime("%m/%Y")
    df = pd.read_csv('Attendance_file.csv')
    print(date)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df2 = df[df['date'].dt.strftime('%m/%Y') == date]
    print(df2)

#print all the employyes that where late last month
def wholate():
    now_date = datetime.now()
    date = now_date.strftime("%m/%Y")
    df = pd.read_csv('Attendance_file.csv')
    print(date)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    df2 = df[(df['date'].dt.strftime('%m/%Y') == date) & (df['time'] > '09:30')]
    print(df2)

#employee enters his id and marks attendance
def markAttendance(_id):
    try:
       # print("Adding a new attendens, please enter the following details\n")
        #employee_id = int(input("Enter your employee ID\n"))
        employee_id = _id
        name = Employees.getname(employee_id)

        now_date = datetime.now()
        date = now_date.strftime("%d/%m/%Y")
        now_time = datetime.now()
        time = now_time.strftime("%H:%M:%S")

        data = ({
            'Id': [employee_id],
            'name': [name],
            'date': [date],
            'time': [time]
        })

        # Make data frame of above data
        df = pd.DataFrame(data)

        # append data frame to CSV file
        df.to_csv('Attendance_file.csv', mode='a', index=False, header=False)

        print("Data appended successfully.")

    except ValueError:
        print("Oops, something went wrong!")