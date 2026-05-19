# first nonrepeating character

def first_non_repeating_char(s: str) -> str | None:
    for i in range(len(s)):
        ch = s[i]
        count = 0
        for j in range(len(s)):
            if s[j] == ch:
                count += 1
        if count == 1:
            return ch

    return None


print(first_non_repeating_char("savans"))

