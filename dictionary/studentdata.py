# Write a program to accept student name and marks from the keyboard and create a dictionary. Also display Student marks by taking student name

n=int(input("Enter the number of students: "))
d={}
for i in range(n):
    name=input("Enter Student name: ")
    marks=input("Enter Student marks: ")
    d[name]=marks   #add student marks
print(d)    
while True:
    name=input("Enter Student name to get marks: ")
    marks=d.get(name,-1)
    if marks==-1:      #checks if student is present in dict or not
        print("Student Not Found")
    else:
        print("The marks of",name,"are",marks)
    option=input("Do you want to find another student marks[Yes?/No]")     
    if option=="No":
        break
        print("Thanks for using our application")
        




