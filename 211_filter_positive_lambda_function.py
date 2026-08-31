numbers = list(map(int, input("Enter numbers: ").split()))

positive_numbers = list(filter(lambda x: x > 0, numbers))

print("Positive numbers:", positive_numbers)
