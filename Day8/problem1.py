#remove leading zeroes

num=[0,0,1,0,2,0,3,0,0,4]
i=0
while i<len(num) and num[i]==0:
    i+=1
num=num[i:]    
print(num)

#output-- [1, 0, 2, 0, 3, 0, 0, 4]