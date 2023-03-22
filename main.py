import Attendant_log
import Employees
import os
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
  if choice==-1:
   Employees.open_file()
  if choice == 0:
     return
  if choice == 1:

    path = input("Enter file name:")

    if os.stat(path).st_size == 0:
        Employees.addemployee(str(path))
    else:
        Employees.addemployee_ifnotempty(str(path))
  if choice == 2:
      path=input("Add employees from path:")
      Employees.addemployeebypath(path)
  if choice == 3:
     id_todelete = int(input("enter employee id:"))
     Employees.removemployee(id_todelete)
  if choice ==4:
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
    print("2.Genarate Attendance report of an employee\n")
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
    if choice ==0:
        start()





start()