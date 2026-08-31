def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, high)

numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter element to search: "))

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)
