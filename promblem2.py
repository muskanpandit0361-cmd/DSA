#i/p--[1,1,0,1,1,1,0,1,1,1,1]
#o/p--4        max no of consecutive 1s in binary array

# num=[1,1,0,1,1,1,0,1,1,1,1]
# count=0
# maximum=0
# for i in num:
#     if i==1:
#         count+=1
#         maximum=max(count,maximum)
#     else:
#         count=0   
# print(maximum)         

#-----------------------------------------

#i/p=="abababab"  and "ab"
#o/t== 4              count number of occurance of substring

string="abababab"
count=0
for i in range(len(string)-1):
    if string[i]=="a" and string[i+1]=="b":
        count+=1
print(count)            

