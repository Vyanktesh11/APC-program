contacts = {
    "Rahul": "9876543210",
    "Amit": "9123456780"
}

contacts["Sneha"] = "9988776655"

name = input("Enter contact to search: ")
if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

name = input("Enter contact to update: ")
if name in contacts:
    contacts[name] = input("Enter new phone number: ")

name = input("Enter contact to delete: ")
if name in contacts:
    del contacts[name]

print("All contacts:")
for name, phone in contacts.items():
    print(name, phone)
