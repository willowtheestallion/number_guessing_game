import random

random_num = random.randint(1, 100)
max_attempts = 7


#range(1, max_attempts + 1) gives you attempt numbers 1 through 7, and the loop ends on its own after the last one.
for attempt in range(1, max_attempts + 1):
    user_input = int(input(f"Attempt {attempt}/{max_attempts} - Type in the guessed number: "))

    if user_input == random_num:
      print(f"Congratulations! You guessed correctly in {attempt} attempts. The number is {random_num}")
    elif user_input > random_num:
      print("Wrong!Go lower")
    elif user_input < random_num:
      print("Wrong!Go higher")
else:
    print(f"Out of attempts. The number is {random_num}")

    
