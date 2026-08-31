morning = {"Rahul", "Amit", "Priya", "Sneha"}
afternoon = {"Priya", "Sneha", "Rohan", "Neha"}

print("Students present in both sessions:", morning & afternoon)
print("Students only in morning:", morning - afternoon)
print("Students only in afternoon:", afternoon - morning)
print("Students in at least one session:", morning | afternoon)
