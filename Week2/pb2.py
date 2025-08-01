import random

number = random.randint(1,10)
user_number = 0
try:
    user_number = int(input(""))
except ValueError:
    print("That's not valid number")
    pass

flag = 1
while flag == 1:
    if user_number < number:
        print("Too low!")
        user_number = int(input(""))
    elif user_number > number:
        print("Too high!")
        user_number = int(input(""))
    elif user_number == number:
        print("Correct!You win!")
        flag = 0

