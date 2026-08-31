def largest(numbers):
    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number

numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest:", largest(numbers))
