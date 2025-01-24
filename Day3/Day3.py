import random

print("Welcome to our Jangi game")
print("You will have to guess a number between 0 to 50")

a = random.randint(0, 5)

x= int(input("Enter the number you think is correct: "))

if x>a:
    print("your number is bigger")
    print("The number was",a,". Try again Later")
elif x<a:
    print("your number is smaller")
    print("The number was",a,". Try again Later")
else:
    print("Congratulation!!. You Had it corrct")
    print("The number is ",x)