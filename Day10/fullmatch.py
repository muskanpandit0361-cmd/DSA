import re
a = input("Enter string to perform match operation: ")
mtch = re.fullmatch(a,"pythonisvery")    #if matches full string , returnsntrue , otherwise false

print(mtch)
if mtch!=None:
    print("match found .")
    print(mtch.start()," ",mtch.end())
else:
    print("Full match not found")  