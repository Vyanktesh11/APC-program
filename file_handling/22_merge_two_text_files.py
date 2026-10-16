with open("file1.txt", "w") as f:
    f.write("Content from file one.\\n")

with open("file2.txt", "w") as f:
    f.write("Content from file two.\\n")

with open("file1.txt", "r") as first, open("file2.txt", "r") as second:
    combined = first.read() + second.read()

with open("combined.txt", "w") as output:
    output.write(combined)

print(combined)
