while True:
    x=input("Enter the number for the multiplication: ")
    if not x.isnumeric :
        print("enter an interger: ")

    else:
        x=int(x)

        for i in range(1,16,1):
                
            y=i*x
            print(i,"*",x,"=",y)
        choice = input("Do you want to exit the code, Enter yes or no: ")
        if choice == "yes":
            print("Thank see you next time")
            break
        else: 
            continue