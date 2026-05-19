#---instance variable-----------

# class New:
#     def __init__(self):
#         self.a=10

# obj1=New()    
# obj2=New()        
# obj3=New()        

# obj1.a=20

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#---static variable-----------

class New:
    a=10

    def __init__(self):
        self.name="prashant"

obj1 = New()        
obj2 = New()        
obj3 = New()        

New.a=50
print(obj1.a)
print(obj2.a)
print(obj3.a)
#-------------------------

class College:
    collegename="Modern College"

    def __init__(self):
        self.studentname="prashant"

principal = College()
teacher=College()
accountant=College()

print("principal=",principal.collegename,"....",principal.studentname)
print("teacher=",teacher.collegename,"....",teacher.studentname)
print("accountant=",accountant.collegename,"....",accountant.studentname)

College.collegename="HBD"
principal.studentname="prashant jha"

print("principal=",principal.collegename,"....",principal.studentname)
print("teacher=",teacher.collegename,"....",teacher.studentname)
print("accountant=",accountant.collegename,"....",accountant.studentname)








