def sets():
    set1 = []  # Initialize an empty lists
    set2= []
    while True:
        print("\n*** Your Lists ***")
        print("1. Add item to list 1")
        print("2. Add item to list 2")
        print("3. Remove item from list 1")
        print("4. Remove item from list 2")
        print("5. Display the intersection of list 1 and list 2")
        print("6. Display the intersection of list 1 and list 2")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            item = input("Enter the item to add: ")
            set1.append(item)  # Add the item to list1
            print(f"'{item}' added to list 1.")
        elif choice == "2":
          item = input("Enter the item to add: ")
          set2.append(item)  # Add the item to list2
          print(f"'{item}' added to list 2.")
        elif choice == "3":
                if not set1:
                    print("Your cart is empty.")
                else:
                    print("\n*** Your Cart ***")
                    for index, item in enumerate(set1, start=1):
                        print(f"{index}. {item}")
                    try:
                        item_number = int(input("Enter the item number to remove: "))
                        if 1 <= item_number <= len(set1):
                            removed_item = set1.pop(item_number - 1)
                            print(f"'{removed_item}' removed from list 1 .")
                        else:
                            print("Invalid item number.")
                    except ValueError:
                        print("Please enter a valid number.")
        elif choice == "4":
                if not set2:
                    print("Your cart is empty.")
                else:
                    print("\n*** Your Cart ***")
                    for index, item in enumerate(set2, start=1):
                        print(f"{index}. {item}")
                    try:
                        item_number = int(input("Enter the item number to remove: "))
                        if 1 <= item_number <= len(set2):
                            removed_item = set2.pop(item_number - 1)
                            print(f"'{removed_item}' removed from list 2 .")
                        else:
                            print("Invalid item number.")
                    except ValueError:
                        print("Please enter a valid number.")
        elif choice == "5":
            s1=set(set1)
            s2=set(set2)
            w = s1.union(s2)
            print(w)

        elif choice == "6":
            s1=set(set1)
            s2=set(set2)
            y = s1.intersection(s2)
            print(y)
        
        elif choice == "7":
            
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


sets()