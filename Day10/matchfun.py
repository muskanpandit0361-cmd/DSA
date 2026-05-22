import re
a = input("Enter string to perform match operation: ")
mtch = re.match(a,"python is very important language")    #used to find first matching object. if found return true, otherwise false

print(mtch)
if mtch!=None:
    print("match found at beginning level.")
    print(mtch.start()," ",mtch.end())
else:
    print("there is no matching at beginning level")    