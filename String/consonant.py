string="magnificient"
check="aeiou"
vowels=""
vow=0
consonant=""
con=0
for i in string:
    if i not in check:
        con+=1
        consonant+=i
    else:
        vow+=1
        vowels+=i    
print(f"vowels:{vow}")
print(vowels)
print(f"consonant:{con}")
print(consonant)        