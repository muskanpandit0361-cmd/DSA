# import re
# count = 0
# pattern = re.compile("python")

# matcher = pattern.finditer("A function in python is defined by a def statement.python the general syntax look like this: def function - name(Parameter list):statements, i.e the function body.The parameter consists of non or more parameters." )

# for i in matcher:
#     count+=1
#     print(i.start(),"--",i.end(),"--",i.group())
# print("The number of occurrences: ",count)    



#---------------------search() function-----------

# import re
# a = input("Enter string to perform match operation: ")
# mtch = re.search(a,"python sss dynamic lannn")    #if matches any string , returns true , otherwise false

# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("There is no matching anywhere")


#---------------------findall() function-----------

# import re
# mtch = re.findall('[0-9A-Z]',"lkfejkf32473265JGHYTFhejrjhrweurw")
# print(mtch)

#for '[0-9a-z]'--['l', 'k', 'f', 'e', 'j', 'k', 'f', '3', '2', '4', '7', '3', '2', '6', '5', 'h', 'e', 'j', 'r', 'j', 'h', 'r', 'w', 'e', 'u', 'r', 'w']
#for '[^0-9a-z]'--['J', 'G', 'H', 'Y', 'T', 'F']
#for [0-9A-Z]'--['3', '2', '4', '7', '3', '2', '6', '5', 'J', 'G', 'H', 'Y', 'T', 'F']

#---------------------sub() function-----------
#to replace

# import re
# obj = re.sub('[a-zA-Z]','X','2323 ABCD fgdf FDgD')
# print(obj)    #output--2323 XXXX XXXX XXXX


#'[a-zA-Z]','X','2323 ABCD fgdf FDgD' -- 2323 XXXX XXXX XXXX
#'[A-Z]','*','2323 ABCD fgdf FDgD' -- 2323 **** fgdf **g*
#'[0-9]','#','2323 ABCD fgdf FDgD' -- #### ABCD fgdf FDgD



#---------------------subn() function-----------

#Replace + returns count 
import re
obj = re.subn('[a-zA-Z]','X','2323 ABCD fgdf FDgD')
print(obj)     #output -- ('2323 XXXX XXXX XXXX', 12)
