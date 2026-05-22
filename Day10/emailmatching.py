import re
s = input("Enter mail id: ")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@(gmail.com|@rbunagpur\.in)",s)
if m != None:
    print("Valid E-Mail Id")
else:
    print("Invalid E-Mail Id")    