words = input("Enter words: ").split()

result = sorted(words, key=lambda word: len(word))

print("Words sorted by length:", result)
