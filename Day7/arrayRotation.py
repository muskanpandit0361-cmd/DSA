#i/p- [1,2,3,4,5]  rotated by step 2
#o/p- [4,5,1,2,3]

list = [1, 2, 3, 4, 5]
k = 3

rotated = list[-k:] + list[:-k]

print(rotated)
