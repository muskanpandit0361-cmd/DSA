import re
obj = input("Enter any character ")
objmatch = re.finditer(obj,"a7b @k9z-")

for match in objmatch:
    print(match.start(),"--",match.end(),"--",match.group())


#output:
# Enter any character a
#0 -- 1 -- a    

# Enter any character  
# 3 -- 4 --  