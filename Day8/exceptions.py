
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Can't divide by zero")    
except ValueError:
    print("Enter only integer values!")    
except:          #default part like else in else-if ladder
    print("ABC") 
finally:
    print("I always execute")    
# else:
#     print("Everthing is OK")      #prints everytime 



#-----------------------    for multiple exceptions in one except block
# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print(a/b)
# except (ZeroDivisionError,ValueError) as msg:
#     print(msg)