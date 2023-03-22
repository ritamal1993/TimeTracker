import os
import pandas as pd
import csv


class Employees:



    def addemployee(path):

        try:
            print("Adding a new employee, please enter the following details\n")
            employee_id = int(input("Enter your employee ID\n"))
            name = input("Enter your name\n")
            phone = input("Enter your phone\n")
            age = int(input("Enter your age\n"))

            data = ({
                'Id': [employee_id],
                'name': [name],
                'phone': [phone],
                'age': [age]
            })

            # Make data frame of above data
            df = pd.DataFrame(data)

            # append data frame to CSV file
            df.to_csv(path, mode='a', index=False, header=True)

            print("Data appended successfully.")

        except ValueError:
            print("Oops, something went wrong!")


# Add employee without header
def addemployee_ifnotempty(path):
    try:
        print("Adding a new employee, please enter the following details\n")
        employee_id = int(input("Enter your employee ID\n"))
        name = input("Enter your name\n")
        phone = input("Enter your phone\n")
        age = int(input("Enter your age\n"))

        data = ({
            'Id': [employee_id],
            'name': [name],
            'phone': [phone],
            'age': [age]
        })

        # Make data frame of above data
        df = pd.DataFrame(data)

        # append data frame to CSV file

        df.to_csv(path, mode='a', index=False, header=False)

        print("Data appended successfully.")

    except ValueError:
        print("Oops, something went wrong!")


# Add employees by path

def addemployeebypath(path):
    try:
        print("Adding a new employees, from file:\n" + str(path))
        data = pd.read_csv(str(path))
        file = input("Adding a new employees, to file you choose print the file name:\n")
        data.to_csv(file, mode='a', index=False, header=False)

    except ValueError:
        print("Oops, something went wrong!")


# Delete employee manually from file the user choose
def removemployee(employee):
    print("removing employee id:\n" + str(employee))
    file = input("deleting..., please write the file name:")
    data = pd.read_csv(file)
    data.set_index('Id', inplace=True)
    data = data.drop(employee, axis=0)
    data.to_csv(file)


# Delete file by path
def deletemployees(path):
    print("Deleting file:\n" + str(path))
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        print("file deleted")
    else:
        print("file not found")


# search employee in specific file
def searchemployee(_id):
    file = input("input file name:")
    df = pd.read_csv(file)
    rslt_df = df[df['Id'] == int(_id)]
    print(rslt_df)


# deleting all the information in the file by path
def deletebypath(path):
    f = open(path, "w+")
    f.close()
    f = open(path, "w+")
    writer = csv.writer(f)
    header = ['Id', 'name', 'phone', 'age']
    # write the header
    writer.writerow(header)


# show all employees from selected file
def showallemployees():
    file = input("input file name with ending format .csv .xls ...:")
    df = pd.read_csv(file)
    print(df)
def open_file():
    path = input("Enter file name:")
    with open(path, 'w') as file:
        writer = csv.writer(file)
        header = ['Id', 'name', 'phone', 'age']
        # write the header
        writer.writerow(header)
        file.close()

def getname(_id):
    df = pd.read_csv('database.csv')
    rslt_df = df[df['Id'] == int(_id)]
    return rslt_df['name'].values[0]