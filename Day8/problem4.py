#col name= StudId | studName | phy |chem | maths | Total | Percentage | Result

#input: StudId, studeName, phy, chem, maths
#calculate: total, percentage
#check condition all paper marks >= 40 pass else fail

import csv

# input
studId = int(input("Enter Student ID: "))
studName = input("Enter Student Name: ")

phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chemistry Marks: "))
maths = int(input("Enter Maths Marks: "))

# calculate total and percentage
total = phy + chem + maths
percentage = total / 3

# result
if phy >= 40 and chem >= 40 and maths >= 40:
    result = "Pass"
else:
    result = "Fail"

# store in csv file
with open("student.csv", "a", newline="") as file:

    writer = csv.writer(file)

    # column names    #comment this after creating file to avoid duplicate columns
    writer.writerow([
        "StudId", "StudName", "Phy",
        "Chem", "Maths", "Total",
        "Percentage", "Result"
    ])

    # data row
    writer.writerow([
        studId, studName, phy,
        chem, maths, total,
        percentage, result
    ])

print("Data stored successfully in student.csv")