# #Single level inheritance

# class College:          #parent class
#     def college_name(self):    #member function
#         print("RBU")

# class Student(College):    #child class
#     def student_info(self):          #member function
#         print("Name: Muskan")   
#         print("Branch: MCA")

# obj = Student()     #object of child class
# obj.college_name()
# obj.student_info()             


#=================================================

# #multilevel inheritance
# class College:          #first class
#     def college_name(self):    #member function
#         print("RBU")

# class Student(College):    #second class
#     def student_info(self):          #member function
#         print("Name: Muskan")   
#         print("Branch: MCA")

# class Exam(Student):        #child class  
#     def subject(self):
#         print("Subject 1: Design Engineering")
#         print("Subject 2: Math")
#         print("Subject 3: C-Language")


# obj = Exam()     #object of child class
# obj.college_name()
# obj.student_info()
# obj.subject()


# #==========================================

# #Multiple inheritance

# class SubjMarks:
#     math = int(input("Enter paper marks of math: "))
#     DE = int(input("Enter paper marks of DE: "))
#     C = int(input("Enter paper marks of C: "))
#     eng = int(input("Enter paper marks of english: "))

# class PractMarks:
#     cpract = int(input("Enter practical marks of C: "))    

# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.C>=40 and self.eng>=40 and self.cpract>=40:
#             print("Pass")
#         else:
#             print("Fail")

# obj = Result()
# obj.total()                


#===================================

class A:
    def display(self):
        print("Class A")

class B:
    def display(self):
        print("Class B") 

class C(A,B):
    def msg(self):
        print("Class C")           

obj = C()
obj.display()              #calls method of class A. No ambiguity as it simply calls the first method encountered. 
obj.msg()        