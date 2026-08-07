numbers = list(map(int, input("Enter numbers: ").split()))

numbers = list(set(numbers))
numbers.sort()

print("Second Largest:", numbers[-2])