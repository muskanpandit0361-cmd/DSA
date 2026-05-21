# class RBI:
#     def home_loan(self):
#         print("Home loan = 8%")

#     def edu_loan(self):
#         print("Education loan = 9%")    

# class SBI(RBI):
#     def edu_loan(self):
#         print("Education loan = 11%")   #overrides
#         super().edu_loan()          #accessing parent class method

# obj = SBI()
# obj.home_loan()
# obj.edu_loan()

#output:
# Home loan = 8%
# Education loan = 11%
# Education loan = 9%

#===================constructor overriding======================

class RBI:
    def __init__(self):
        print("Parent class constructor")

class SBI(RBI):
    def __init__(self):
        print("Child class constructor")         #overrides parent class constructor 
        super().__init__()
        
obj = SBI()
