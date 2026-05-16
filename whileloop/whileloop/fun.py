# i=1
# while i<=5:     #syntax
#     print(i)
#     i+=1

#-----------------------------

#--------functions------------

# def hello():           #--------------->called function
#     print("Hello World")

# hello()                #--------------->calling fuction

#----------

# def arithmetic():
#     a=int(input("Enter the value of a: "))
#     b=int(input("Enter the value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# #print(arithmetic())           #returns Enter the value of a: 50
#                                   # Enter the value of b: 10
# result=arithmetic()                                   #(60, 40, 5.0, 500)    it is possible to print multiple values in python using this way
# print(result)                                   #it returned values in tuple because it won't change during runtime

#---------------------------------------------------------------

# types of argument pass in a funtion:
# 1. Positional argument
# 2. keyword argument
# 3. default argument
# 4. variable length argument/ variable number of arguments

# 1. Positional argument  (input passing)
# def arithmetic(a,b):
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# result=arithmetic(10,2)  
# print(result)   


# 2. keyword argument
# def credential(username,password):
#     if username==password:
#         print("Login Successfully")
#     else:
#         print("Invalid Credentials")
# credential(username="abc", password="abcd")   

# 3. default argument
# def CityName(city="Pune"):
#     print(city)
# CityName("Nagpur")
# CityName("Mumbai")
# CityName()    #-----------> when no argument is passed, calls default argument


# 4. variable length argument/ variable number of arguments
# def CityName(*city):     #---------> "*" ensures multiple arguments can be passed
#     print(city)

# CityName("Nagpur","Mumbai","Pune")

#==============================================
#modularity approach in fuctions

import sys         #-----> for using exit()
def add():
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    print(a+b)

def sub():
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    print(a-b)

def mul():
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    print(a*b)   

def div():
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    print(a/b)     
 

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        sys.exit()
        