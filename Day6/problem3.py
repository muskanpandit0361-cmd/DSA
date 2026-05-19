numbers = list(map(int, input("Enter the numbers: ").split()))
result = {}
count=[]
for num in numbers:
    if num in result:
        result[num] += 1
    else:
        result[num] = 1
for num in result:
    if result[num]>1:
        count.append(num)
print(count)        

