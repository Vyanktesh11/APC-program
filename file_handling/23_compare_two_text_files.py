first_name = input("First filename: ")
second_name = input("Second filename: ")

with open(first_name, "r") as f:
    first_lines = f.readlines()

with open(second_name, "r") as f:
    second_lines = f.readlines()

if first_lines == second_lines:
    print("Files are identical.")
else:
    print("Files are different.")
    limit = min(len(first_lines), len(second_lines))
    for index in range(limit):
        if first_lines[index] != second_lines[index]:
            print("First difference at line", index + 1)
            print("First file:", first_lines[index].rstrip())
            print("Second file:", second_lines[index].rstrip())
            break
    else:
        print("One file has extra lines.")
