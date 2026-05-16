# import datetime

# date=datetime.datetime.now()
# print("Its now:{:%d/%m/%Y %H:%M:%S}".format(date))


# #--------------------

# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3]
# print(x==y)
# print(x==z)
# print(x!=z)

#--------------------
#list comprehension
# val=[2**i for i in range(1,6)]
# print(val)

#--------------------

# val=[i*i for i in range(1,11)]
# print(val)

#-----------------
#dictionry comprehension
# squares={i:i*i for i in range(1,11)}
# print(squares)

#-----------------

# double={i:2*i for i in range(1,11)}
# print(double)

#returns {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}

#------------------

# a,b=[int(x) for x in input("Enter 2 numbers: ").split()]
# print("Product:",a*b)

#o/t:
#  Enter 2 numbers: 3 8
#  Product: 24
#------------------

# a,b,c=[float(x) for x in input("Enter 3 float numbers: ").split(',')]
# print("Sum:",a+b+c)

#o/t:
# Enter 3 float numbers: 3.4 2.5 5.6
# Sum: 11.5

#------------

mycart=[10,20,800,60,70]
for item in mycart:
    if item>400:
        print("this is not in my budget")
        continue
    print(item)
else:
    print("you have purchased everthing")    


#else is possible with for block in python

#--------------------------------
correct_username = "admin"
correct_password = "admin"

username = ""
password = ""

while username != correct_username or password != correct_password:
    username = input("Enter username: ")
    password = input("Enter password: ")
    

print("Login successful")
