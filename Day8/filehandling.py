#to create and store data in csv file

import csv
f=open("employee.csv",'a')
a=csv.writer(f)
#a.writerow(["EmpID","EmpName","EmpAge"])           #to create columns
empid=int(input("Enter your EmpID: "))
empname=input("Enter employee age: ")
age=int(input("Enter employee age: "))
a.writerow([empid,empname,age])
print("File has created")