with open("student.txt", "r") as f:
    words = f.read().lower().split()

frequency = {}
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        frequency[word] = frequency.get(word, 0) + 1

print(frequency)
