#Insertion sort

arr=[5,3,8,6,2]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while  j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
            print(arr)
    arr[j+1]=key   
    print(arr)
    print("-------")    
i+=1        
print("Sorted array: ",arr)

        
#output:
# [5, 5, 8, 6, 2]
# [3, 5, 8, 6, 2]
# -------
# [3, 5, 8, 6, 2]
# -------
# [3, 5, 8, 8, 2]
# [3, 5, 6, 8, 2]
# -------
# [3, 5, 6, 8, 8]
# [3, 5, 6, 6, 8]
# [3, 5, 5, 6, 8]
# [3, 3, 5, 6, 8]
# [2, 3, 5, 6, 8]
# -------
# Sorted array:  [2, 3, 5, 6, 8]
