import logging
logging.basicConfig(filename="logfile.txt", level=logging.DEBUG)
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except (ZeroDivisionError,ValueError) as msg:
    print(msg)
    logging.exception(msg)
print("Logging level is set up. Check 'logfile.txt' for log details.")    
