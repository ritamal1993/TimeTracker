import os
import pandas as pd
import csv


class Employees:

     def addemployee(self,employee_id,name,phone,age):

       # try:
          #  print("Adding a new employee, please enter the following details\n")
           # employee_id = int(input("Enter your employee ID\n"))
           # name = input("Enter your name\n")
           # phone = input("Enter your phone\n")
           # age = int(input("Enter your age\n"))

            data = ({
                'Id': [employee_id],
                'name': [name],
                'phone': [phone],
                'age': [age]
            })

            # Make data frame of above data
            df = pd.DataFrame(data)

            # append data frame to CSV file
            df.to_csv('data.csv', mode='a', index=False, header=True)

           # print("Data appended successfully.")

      #  except ValueError:
          #  print("Oops, something went wrong!")


# Add employee without header
def addemployee_ifnotempty(employee_id,name,phone,age):
    try:
      #  print("Adding a new employee, please enter the following details\n")
       # employee_id = int(input("Enter your employee ID\n"))
        #name = input("Enter your name\n")
        #phone = input("Enter your phone\n")
        #age = int(input("Enter your age\n"))


        data = ({
            'Id': [employee_id],
            'name': [name],
            'phone': [phone],
            'age': [age]
        })

        # Make data frame of above data
        df = pd.DataFrame(data)

        # append data frame to CSV file
        if os.stat('database.csv').st_size == 0:
         _header = True
        else:
         _header = False
        df.to_csv('database.csv', mode='a', index=False, header=_header)

        print("Data appended successfully.")

    except ValueError:
        print("Oops, something went wrong!")


# Add employees by path

def addemployeebypath(path):
    try:
        print("Adding a new employees, from file:\n" + str(path))
        data = pd.read_csv(str(path))
        #file = input("Adding a new employees, to file you choose print the file name:\n")
        data.to_csv('database.csv', mode='a', index=False, header=False)

    except ValueError:
        print("Oops, something went wrong!")


# Delete employee manually from file the user choose
def removemployee(employee):
    #print("removing employee id:\n" + str(employee))
   #file = input("deleting..., please write the file name:")
    data = pd.read_csv('database.csv')
    data.set_index('Id', inplace=True)
    data = data.drop(int(employee), axis=0)
    data.to_csv('database.csv')


    data1 = pd.read_csv('Attendance_file.csv')
    data1.set_index('Id', inplace=True)
    data1 = data.drop(int(employee), axis=0)
    data1.to_csv('Attendance_file.csv')


# Delete file by path
def deletemployees(path):
    print("Deleting file:\n" + str(path))
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        print("file deleted")
    else:
        print("file not found")


# search employee in specific file
def searchemployee(_id,file):

    df = pd.read_csv(file)
    rslt_df = df[df['Id'] == int(_id)]
    if(rslt_df.empty):
        print("id not found in the data base")
    else:
        return rslt_df


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
 try:
    file = input("input file name with ending format .csv .xls ...:")
    df = pd.read_csv(file)
    print(df)
 except FileNotFoundError:
     print("file not found")
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







