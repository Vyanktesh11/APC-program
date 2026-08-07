s = input("Enter a string: ")

r = ""
c = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        c += 1
    else:
        r += s[i - 1] + str(c)
        c = 1

r += s[-1] + str(c)

if len(r) < len(s):
    print(r)
else:
    print(s)