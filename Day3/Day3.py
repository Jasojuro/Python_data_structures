import random

print("Welcome to our Jangi game")
print("You will have to guess a number between 0 to 10")

a = random.randint(0, 10)

x= int(input("Enter the number you think is correct: "))

while a!=x:

    if x>a:
        print("your number is bigger")
        print("Try again Later")
        continue
        
    elif x<a:
        print("your number is smaller")
        print("The number was",a,". Try again Later")
        
    else:

        print("Congratulation!!. You Had it corrct")
        print("The number is ",x)
        break
