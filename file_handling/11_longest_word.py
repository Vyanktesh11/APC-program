with open("student.txt", "r") as f:
    words = f.read().split()

longest = max(words, key=len) if words else ""
print("Longest word:", longest)
