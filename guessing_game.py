import random

random_num = random.randint(1, 100)

user_input = int(input("Type in the guessed number: "))

while user_input != random_num:
    if user_input > random_num:
      print("Wrong! Go lower.")
    else:
       print("Wrong! Go higher.")
    user_input = int(input("Try again: "))

print(f"You've guessed correctly. The number is {random_num}")