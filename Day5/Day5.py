
def add():
    total=0
    while True:
        u_input = input("Enter a number to add ( type 'done' to stop):  ")#permits the user to enter all the needed to be added until "done" is entered
        if u_input=="done":
            break
        try:
            number=float(u_input)
            total += number
        except ValueError:
            input("Enter an interger: ")
    return total


def sub():
    total=None
    while True:
        u_input = input("Enter a number to subtract ( type 'done' to stop):  ")#permits the user to enter all the needed to be added until "done" is entered
        if u_input=="done":
            break
        try:
            number=float(u_input)
            if total is None:
                total=number
            else:
                total -= number
        except ValueError:
            input("Enter an number: ")
    return total

def mul():
    total=None
    while True:
        u_input = input("Enter a number to multiply ( type 'done' to stop):  ")#permits the user to enter all the needed to be added until "done" is entered
        if u_input=="done":
            break
        try:
            number=float(u_input)
            if total is None:
                total=number
            else:
                total *= number
        except ValueError:
            input("Enter an number: ")
    return total

def div():
    total=None
    while True:
        u_input = input("Enter a number to divide ( type 'done' to stop):  ")#permits the user to enter all the needed to be added until "done" is entered
        if u_input=="done":
            break
        try:
            number=float(u_input)
            if total is None:
                total=number
            else:
                if number==0:
                    raise TypeError("Division by 0 is not possible")
                total /= number
        except ValueError:
            input("Enter an number: ")
        
            
    return total

print("Enter 1 for Addition, 2 for subtraction, 3 for multiplication,4 for division ")
Operation = input("What operation do you want to perform?: ")

match Operation:
    case "1":
        sum=add()
        print(f"The sum of the numbers is : {sum}")
    case "2":
        diff=sub()
        print(f"The difference of the numbers is : {diff}")
    case "3":
        prod=mul()
        print(f"The product of the numbers is : {prod}")
    case "4":
        quo=div()
        print(f"The quotient of the numbers is : {quo}")
    




        
