
import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem      A=[3,2,1]  B=[]  C=[]")
        print()
        print("Expected Output    A=[]       B=[]  C=[3,2,1]")
        self.A = []
        self.B = []
        self.C = []

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"   ",   "B=",self.B   ,"    ","C=",self.C)
        print("Pass 1 completed==========\n")   

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"   ",   "B=",self.B   ,"    ","C=",self.C)
        print("Pass 2 completed==========\n")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"   ",   "B=",self.B   ,"    ","C=",self.C)
        print("Pass 3 completed==========\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"   ",   "B=",self.B   ,"    ","C=",self.C)
        print("Pass 4 completed==========\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"   ",   "B=",self.B   ,"    ","C=",self.C)
        print("Pass 5 completed==========\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "   ", "B=", self.B, "   ", "C=", self.C)
        print("Pass 6 completed==========\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=", self.A, "   ", "B=", self.B, "   ", "C=", self.C)
        print("Pass 7 completed==========\n") 

t = Tower()

t.tower(3)
t.tower(2)
t.tower(1)

t.pass1()
t.pass2()
t.pass3()
t.pass4()
t.pass5()
t.pass6()
t.pass7()           
