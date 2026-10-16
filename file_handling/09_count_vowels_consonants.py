with open("student.txt", "r") as f:
    text = f.read().lower()

vowels = sum(ch in "aeiou" for ch in text)
consonants = sum(ch.isalpha() and ch not in "aeiou" for ch in text)

print("Vowels:", vowels)
print("Consonants:", consonants)
