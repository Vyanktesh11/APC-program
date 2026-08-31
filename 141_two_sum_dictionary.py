numbers = list(map(int, input("Enter integers: ").split()))
target = int(input("Enter target: "))

seen = {}
found = False

for num in numbers:
    complement = target - num

    if complement in seen:
        print("Two numbers:", complement, num)
        found = True
        break

    seen[num] = True

if not found:
    print("No pair found")
