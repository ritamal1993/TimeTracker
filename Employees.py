import os

import pandas as pd


class Employees:
    def __init__(self, employee_id, name, phone, age):
        self.employee_id = employee_id
        self.name = name
        self.phone = phone
        self.age = age



# Add employee manualy
# The user can choose to add a new employee to employee files if all the data is supplied
# guven an error message to the user if something is wrong


def addemployee():

    try:
        print("Adding a new employee, please enter the following details\n")
        employee_id = int(input("Enter your employee ID\n"))
        name = input("Enter your name\n")
        phone = input("Enter your phone\n")
        age = input("Enter your age\n")

        data = ({
            'Id': [employee_id],
            'name': [name],
            'phone': [phone],
            'age': [age]
        })

        # Make data frame of above data
        df = pd.DataFrame(data)

        # append data frame to CSV file

        df.to_csv('database.csv', mode='a', index=False, header=True)
       # else:
         #  df.to_csv('database.csv', mode='a', index=False, header=False)

        # print message



        print("Data appended successfully.")

    except ValueError:
        print("Oops, something went wrong!")

def addemployee_ifnotempty():

    try:
        print("Adding a new employee, please enter the following details\n")
        employee_id = int(input("Enter your employee ID\n"))
        name = input("Enter your name\n")
        phone = input("Enter your phone\n")
        age = input("Enter your age\n")

        data = ({
            'Id': [employee_id],
            'name': [name],
            'phone': [phone],
            'age': [age]
        })

        # Make data frame of above data
        df = pd.DataFrame(data)

        # append data frame to CSV file

        df.to_csv('database.csv', mode='a', index=False, header=False)
       # else:
         #  df.to_csv('database.csv', mode='a', index=False, header=False)

        # print message



        print("Data appended successfully.")

    except ValueError:
        print("Oops, something went wrong!")

# Add employee from file

def addemployeebypath(path):
    try:
        print("Adding a new employees, from file:\n" + str(path))
        data = pd.read_csv(str(path))
        data.to_csv('database.csv', mode='a', index=False, header=False)

    except ValueError:
        print("Oops, something went wrong!")


# Delete employee manually
def removemployee(employee):
    print("removing %, from file:\n" + str(employee))
    data = pd.read_csv('database.csv')
    data.set_index('Id', inplace=True)
    data = data.drop(str(employee), axis=0)
    data.to_csv('database.csv')


# Delete employees from file
def deletemployees(path):
    print("Deleting file:\n" + str(path))
    if (os.path.exists(path) and os.path.isfile(path)):
        os.remove(path)
        print("file deleted")
    else:
        print("file not found")



def searchemployee(id):
    df = pd.read_csv('database.csv')
    df.set_index('Id', inplace=True)
    print(df[id])


def deletebypath(path):
    f = open(path, "w+")
    f.close()

def showallemployees():
    df = pd.read_csv('database.csv')
    print(df)
