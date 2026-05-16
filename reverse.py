# num=123456   # ->654321
# a=num%10         #a=6
# num = num//10    #num=12345    '//' returns integer ans of division
# b=num%10         #b=5
# num = num//10    #num=1234
# c=num%10         #c=4
# num = num//10    #num=123
# d=num%10         #b=3
# num = num//10    #num=12
# e=num%10         #b=2
# f=num//10        #num=1
# print(a*100000+b*10000+c*1000+d*100+e*10+f)    #(600000+50000+4000+300+20+1)

#---------------------------------------------

#Bank Cash Calculation System 

Amount=int(input("Enter the amount: "))
print("100 notes= ",Amount//100)
print("50 notes= ",(Amount%100)//50)
print("20 notes= ",((Amount%100)%50)//20)
print("10 notes= ",(((Amount%100)%50)%20)//10)
print("5 notes= ",((((Amount%100)%50)%20)%10)//5)
print("2 notes= ",(((((Amount%100)%50)%20)%10)%5)//2)
print("1 notes= ",((((((Amount%100)%50)%20)%10)%5)%2)//1)
