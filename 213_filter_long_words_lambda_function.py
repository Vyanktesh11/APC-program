words = input("Enter words: ").split()

result = list(filter(lambda word: len(word) > 5, words))

print("Words having more than five characters:", result)
