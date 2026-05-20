#--------------------problem 1-----------------

# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)

# print(factorial(5))

# #--------------------problem 2-----------------

# def capitalizeFirst(arr):

#     result=[]
#     if len(arr)==0:
#         return result
    
#     result.append(arr[0][0].upper()+arr[0][1:])   #capital+slicing   'C'+'ar'              0       1
#     return result+capitalizeFirst(arr[1:])    #same process for remaining elements  arr=['taco','banana']

# print(capitalizeFirst(['car','taco','banana']))

# #--------------------problem 3-----------------

# def power(base, exponent):
#     if exponent==0:
#         return 1
#     return base*(power(base,exponent-1))

# print(power(2,2))

# #--------------------problem 4-----------------

# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1,4,3,8]))

# #--------------------problem 5-----------------

def reverse(string):
    if len(string)<=1:
        return string
    return string[len(string)-1]+reverse(string[0:len(string)-1])

print(reverse("python"))

# #--------------------problem 6-----------------
def recursiverange(num):
    if num<=0:
        return 0
    return num+recursiverange(num-1)

print(recursiverange(6))

# #--------------------problem 7-----------------

def isPalindrom(string):
    if len(string)==0:
        return True
    if string[0]!=string[len(string)-1]:
        return False
    return isPalindrom(string[1:-1])

print(isPalindrom("flower"))
print(isPalindrom("tacocat"))

# #--------------------problem 8-----------------
