s = input("Enter a string: ")

v = c = d = sp = sc = 0

for i in s:
    if i.lower() in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1
    elif i.isdigit():
        d += 1
    elif i == " ":
        sp += 1
    else:
        sc += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)
print("Special Characters:", sc)