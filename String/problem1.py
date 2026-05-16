input="gasgg54@#vscsd!s*" #count number of special characters
output=0
special="@#!$%*&()~^ "
for i in input:
    if i in special:
        output+=1
print(output)        


var="gasgg54@#vscsd!s*"
count=0
for i in var:
    z=ord(i)
    if z>97 and z<=122:
        count=0
    else:
        count+=1
print(count)            


str="this is a test"
print(str.title())
