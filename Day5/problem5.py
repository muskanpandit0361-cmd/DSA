# i/p=6 30 50 
# 29 38 12 48 39 55
# o/p=38 48 39

x,y,z=map(int,input().split())
mylist=[]
for i in range(x):
    a=int(input())
    mylist.append(a)

for j in mylist:
    if j>=y and j<=z:
        print(j, end=" ")    