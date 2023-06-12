print("Welcome to the Shopping Cart Program!")

action = None
names = []
prices = []

while action != "6":
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Empty cart")
    print("5. Compute total")
    print("6. Quit")
    action = input("Please enter an action: ")

    if action == "1":
        name = input("What item would you like to add? ")
        names.append(name)

        price = input(f"What is the price of '{name}'? ")
        prices.append(float(price))

        print(f"'{name}' has been added to the cart.")

    elif action == "2":
        print("The conents of the shopping cart are: ")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${prices[i]:.2f}")

    elif action == "3":
        removed = int(input("Which item would you like to remove? "))
        index = removed - 1

        if index in range(len(names)):
            names.pop(index)
            prices.pop(index)
            print("Item removed.")
        else:
            print("No item in the cart with this number.")

    elif action == "4":
        names.clear()
        prices.clear()
        print("Cart has been emptied.")

    elif action == "5":
        total = 0
        for i in range(len(names)):
            total += prices[i]
        print(f"The total price of the items in the shopping cart is ${total:.2f}")

    else:
        print("Please enter a valid action.")

print("Thank you. Goodbye.")