#input=="Hello World"
#output=="olleH dlrow"

str=input("Enter the string to reverse: ")
x, y = str.split()
print(x)
print(y)
x_rev=""
y_rev=""
for i in range(len(x)-1,-1,-1):
    x_rev+=x[i]
for i in range(len(y)-1,-1,-1):
    y_rev+=y[i]    
print(x_rev+" "+y_rev)    