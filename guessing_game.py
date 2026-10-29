import random

random_num = random.randint(1, 100)

user_input = int(input("Type in the guessed number: "))

if user_input == random_num:
    print("Congratulations, you have guessed correctly.")
elif user_input > random_num:
    print("Wrong! Go lower.")
elif user_input < random_num:
    print("Wrong! Go higher.")
