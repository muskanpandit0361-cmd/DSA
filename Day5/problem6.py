v=['a','e','i','o','u']
w=input("Enter the word: ")
found=[]
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print("Found vowels: ",found)
print("Unique vowels",len(found),"from the given word=",w)        

