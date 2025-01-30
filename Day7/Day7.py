def contact():
    dict={}
    while True:
        print("\n*** Your Contact List ***")
        print("1. Add a Contact")
        print("2. View a Contact")
        print("3. Exit")
        choice = input("Enter your choice (1 or 3): ")

        if choice == "1":
            name = input("Enter the name associated to the contact to be added: ")
            cont =input("Enter the contact to add: ")
            dict[name]=cont #the name and the contact are being added to the dictionary
        
        elif choice == "2":
             if not dict:
                print("Your contact list is empty.") #If dictionary is empty returns "Your contact list is empty"

             else:
                name = input("Enter the name associated to the contact to retrieve: " )
                print("\n*** This is the contact ***")
                print(f"{name}----{dict.get(name)}")#Displays the name(key) and the contact(value) associated to it.

        elif choice == "3":
            print("Thank you for using the contact book. Goodbye!")
            break

        else:
         print("Invalid choice. Please enter a number between 1 and 3.")


contact()
         
        

           


           