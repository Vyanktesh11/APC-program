target = input("Enter word to search: ").lower()
count = 0

with open("student.txt", "r") as f:
    for line_number, line in enumerate(f, start=1):
        matches = [word.strip(".,!?;:\"'()[]{}").lower()
                   for word in line.split()]
        occurrences = matches.count(target)
        if occurrences:
            print("Found on line:", line_number)
            count += occurrences

print("Total occurrences:", count)
