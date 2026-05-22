import re

file = open("paragraph.txt", "r")

text = file.read()

file.close()

word = input("Enter word to search: ")

matches = re.finditer(word, text)

count = 0

for m in matches:
    print("Found at index:", m.start(),"--",m.end(),"--",m.group())
    count += 1

print("Total Count:", count)

#output:
# Enter word to search: Python
# Found at index: 0 -- 6 -- Python
# Found at index: 185 -- 191 -- Python
# Found at index: 356 -- 362 -- Python
# Found at index: 477 -- 483 -- Python
# Found at index: 590 -- 596 -- Python
# Total Count: 5

# Enter word to search: and
# Found at index: 21 -- 24 -- and
# Found at index: 136 -- 139 -- and
# Found at index: 224 -- 227 -- and
# Found at index: 346 -- 349 -- and
# Found at index: 412 -- 415 -- and
# Found at index: 432 -- 435 -- and
# Found at index: 441 -- 444 -- and
# Found at index: 516 -- 519 -- and
# Found at index: 649 -- 652 -- and
# Total Count: 9