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







def report_emp():
    print("Adding a new attendance, please enter the following details\n")
    _id = int(input("Enter your employee ID\n"))
    Employees.searchemployee(_id)



def printall(date):
    df = pd.read_csv('Attendance_file.csv')
    rslt_df = df[df['date'] <= date]
    print(rslt_df)


def wholate():
    return None


def markAttendance():
    try:
        print("Adding a new attendens, please enter the following details\n")
        employee_id = int(input("Enter your employee ID\n"))

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