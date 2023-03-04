
import pandas as pd
class Employees:
    def __init__(self, employee_id, name, phone,age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age=age

#Add employee manualy
#The user can choose to add a new employee to employee files if all the data is supplied
#guven an error message to the user if something is wrong


def addemployee():
        try:
            print("Adding a new employee, please enter the following details\n")
            employee_id = int(input("Enter your employee ID\n"))
            name = input("Enter your name\n")
            phone = input("Enter your department\n")
            age = input("Enter your age\n")


            with open('database.csv', "a") as f:
                employee_info = ""
                employee_info += "%s," % employee_id
                employee_info += "%s," % name
                employee_info += "%s," % phone
                employee_info += "%s," % age
                employee_info += "\n"
                f.write(employee_info)

        except ValueError:
            print("Oops, something went wrong!")







#Add employee from file

def addemployeebypath(path):
    print("Adding a new employees, from path:\n"+str(path))
    data = pd.read_csv(str(path))
    data.to_csv('database.csv')



#Delete employee manually
def removemployee():
    return



#Delete employees from file
def deletemployees():
    return


def searchemployee():
    return


def deletebypath():
    pass
