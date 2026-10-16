from string_utils import count_vowels, reverse_string, is_palindrome, count_words, remove_spaces

s = input("Enter text: ")
print("Vowels:", count_vowels(s))
print("Reverse:", reverse_string(s))
print("Palindrome:", is_palindrome(s))
print("Words:", count_words(s))
print("Without spaces:", remove_spaces(s))
