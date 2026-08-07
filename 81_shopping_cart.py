cart = []

while True:
    print("1.Add Item")
    print("2.Remove Item")
    print("3.Search Item")
    print("4.Display Cart")
    print("5.Count Total Items")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
        else:
            print("Item not found")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print("Item Found")
        else:
            print("Item Not Found")

    elif choice == 4:
        print(cart)

    elif choice == 5:
        print("Total Items:", len(cart))

    elif choice == 6:
        break

    else:
        print("Invalid Choice")