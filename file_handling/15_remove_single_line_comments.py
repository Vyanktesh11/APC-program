source_file = input("Python source filename: ")
output_file = input("Output filename: ")

with open(source_file, "r") as source, open(output_file, "w") as output:
    for line in source:
        if line.lstrip().startswith("#"):
            continue
        output.write(line)

print("Full-line comments removed.")
