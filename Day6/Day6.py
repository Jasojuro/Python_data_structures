def shop():
    cart = []  # Initialize an empty shopping cart (list of items)
    while True:
        print("\n*** Your Shopping Cart ***")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            cart.append(item)  # Add the item to the cart
            print(f"'{item}' added to cart.")

        elif choice == "2":
            if not cart:
                print("Your cart is empty.")
            else:
                print("\n*** Your Cart ***")
                for index, item in enumerate(cart, start=1): # Enumerates the items in cart starting from 1
                    print(f"{index}. {item}")

        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                print("\n*** Your Cart ***")
                for index, item in enumerate(cart, start=1):
                    print(f"{index}. {item}")
                try:
                    item_number = int(input("Enter the item number to remove: "))
                    if 1 <= item_number <= len(cart):
                        removed_item = cart.pop(item_number - 1)
                        print(f"'{removed_item}' removed from cart.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Thank you for using the shopping cart. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


shop()