#i/p= abcdfjgerj  abcdfjger
#o/t= j

str="abcdfjgerj abcdfijger"
p1="" 
p2=""
i=0
while i<len(str):
    if str[i]==" ":
        i+1
        break
    p1+=str[i]

while i < len(str):
    p2 += str[i]
    i += 1

print(p1)
print(p2)


