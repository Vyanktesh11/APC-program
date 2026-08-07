s = input("Enter a sentence: ")

w = s.split()

for i in range(len(w) - 1, -1, -1):
    print(w[i], end=" ")