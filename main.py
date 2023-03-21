import Attendant_log
import Employees
import pandas as pd



def menu():
  print("Welcome to the Employee database\n")
  print("1. Add a new employee\n")
  print("2. add by path existing employee\n")
  print("3. delete employees by id \n")
  print("4. Search and display the details for a particular employee\n")
  print("5. delete file by path\n")
  print("6. show all employees\n")
  print("7. deleting employees from file\n")
  print("0. Quit\n")

  choice = int(input("Please select an option using the numbers above"))
  if choice == 0:
     return
  if choice == 1:
     data = pd.read_csv('database.csv')
     if(data.empty):
         Employees.addemployee()
     else:
         Employees.addemployee_ifnotempty()



  if choice == 2:
      path=input("Add employees from path:")
      Employees.addemployeebypath(path)
  if choice == 3:
     id_todelete = int(input("enter employee id:"))
     Employees.removemployee(id_todelete)
  if choice ==4:
      id_todelete = int(input("enter employee id:"))
      Employees.searchemployee(id)
  if choice == 5:
      path = input("deleting file name:")
      Employees.deletemployees(path)
  if choice == 6:
     Employees.showallemployees()
  if choice == 7:
     path = input("deleting employees from path:")
     Employees.deletebypath(path)

menu()
