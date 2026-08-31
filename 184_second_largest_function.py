def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()

    if len(unique) < 2:
        return None

    return unique[-2]

numbers = list(map(int, input("Enter numbers: ").split()))
result = second_largest(numbers)

if result is None:
    print("Second-largest number does not exist")
else:
    print("Second-largest:", result)
