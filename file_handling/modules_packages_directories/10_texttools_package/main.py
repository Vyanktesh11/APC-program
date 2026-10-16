from texttools.cleaning import clean_text
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = clean_text(input("Enter text: "))
words = tokenize(text)
print("Tokens:", words)
print("Word frequency:", word_frequency(words))
