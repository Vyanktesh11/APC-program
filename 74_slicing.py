numbers = list(map(int, input("Enter 10 numbers: ").split()))

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
numbers = list(map(int, input("Enter numbers: ").split()))

reverse_list = numbers[::-1]

print(reverse_list)