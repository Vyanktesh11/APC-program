words = input("Enter words: ").split()

lengths = list(map(lambda word: len(word), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))

print("Length of every word:", lengths)
print("Words having more than five characters:", long_words)
print("Words sorted by length:", sorted_words)
