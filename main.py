import Attendant_log
import Employees




def menu():
  print("Welcome to the Employee database\n")
  print("1. Add a new employee\n")
  print("2. add by path existing employee\n")
  print("3. delete employees \n")
  print("4. Search and display the details for a particular employee\n")
  print("5. delete by Employee path\n")
  print("0. Quit\n")

  choice = int(input("Please select an option using the numbers above"))
  if choice == 0:
     return
  if choice == 1:
     Employees.addemployee()
  if choice == 2:
      path=input("Add employees from path:")
      Employees.addemployeebypath(path)
  if choice == 3:
     id_todelete = int(input("enter employee id:"))
     Employees.removemployee(id_todelete)
  if choice ==4:
      id_todelete = int(input("enter employee id:"))
      Employees.searchemployee()
  if choice == 5:
      Employees.deletebypath()
  if choice == 6:
     Employees.showallemployees()

menu()
