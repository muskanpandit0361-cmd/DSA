name="Muskanpandit"

print(name[0])
print(name[1])
print(name[-1])
#print(name[15])
print(name[0:5]) #end=-1, 5-1=4
print(name[1:])   #
print(name[:5])   #5-1=4
print(name[:])
print(name[1:8:2])  #8-1=7, increament by 2
print(name[::-1])   #reverse 

#---------------------------------
s="Python is High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())     #upper->lower & vice versa
print(s.title())        #first letter of each word capital
print(s.capitalize())  #only first letter capital
#---------------------------------

name="Muskan"
sal=50000
age=23
print("{} sal is {} age is {}".format(name,sal,age))
print("{0} sal is {1} age is {2}".format(name,sal,age))
print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
print(f"{name} is a good girl")

#-------------------------
name="Muskan"
for i in name:  #for loop starts from 0 
    print(i)
#------------------------
#i/p = "prashant"
# o/p= prasnt    remove duplicate characters
name="prasant"
newname=""
for i in name:
    if i not in newname:  #checks for duplicate
        newname+=i  #add each unique to empty newname
print(newname)        

#------------------
name="prasant"
n=len(name)
newname=""
for i in range(n-1,-1,-1):  #(start,end/cond,inc/dec)
    newname+=name[i]
print(newname)    
#------------------------

a=50
b=30
c=20
d=10
print((a+b)*c/d)
print((a-b)*(c/d))
print(a+(b*c)/d)
          