import random

print("Welcome to our Jangi game")
print("You will have to guess a number between 0 to 10")
a = random.randint(0, 10)

i=0
while i<3:
    x= int(input("Enter the number you think is correct: "))
    if x==a:
        print("Congratulation!!. You Had it corrct")
        break
    else:
        print("Your number is incorrect")
        
        i+=1
if i==3:
    print("The numebr was",a)