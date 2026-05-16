# Write a program to access each character of string in forward and backward direction by using while loop.

string="Learning python is very easy"
n=len(string)
i=0
print("Forward direction:")
while i<n:
    print(string[i],end='')
    i+=1
print()

i=-1
print("Backward direction:")
n=len(string)-1
while i >= -n:
    print(string[i], end='')
    i=i-1    

