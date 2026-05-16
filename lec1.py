#refer DSA_lec1.py for notes
# def findBiggestNo(sampleArray):          #==>O(1)
#     biggestNo=sampleArray[0]             #==>O(1)
#     for index in range(1,len(sampleArray)):    #==>O(N)
#         if sampleArray[index]>biggestNo:       #==>O(1)
#             biggestNo=sampleArray[index]       #==>O(1)
#     print(biggestNo)                           #==>O(1)


# sampleArray=[5,2,8,4,9,0]                      #==>O(1)
# findBiggestNo(sampleArray)                     #==>O(1)

#===========
#O(1)+O(1)+O(1)+O(1)+O(1)+O(1)+O(1)+O(N)=>  O(N)

#======================Linear Search==========================
def linearSearch(array,target):       #==>O(1)
    for i in range(0,len(array)):     #==>O(N)
        if array[i]==target:           #==>O(1)
            return i                   #==>O(1)
    return -1                          #==>O(1)
    
array =[1,2,3,4,5,7,9]
target =7
result=linearSearch(array,target)
if result==-1:
    print("Element not found")
else:
    print("Element found at index ",result)    

 #total=O(N)   