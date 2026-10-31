import random

random_num = random.randint(1, 100)

max_attempts = 7
attempt = 1


#range(1, max_attempts + 1) gives you attempt numbers 1 through 7, and the loop ends on its own after the last one.
while attempt <= max_attempts:
    try:
      user_input = int(input(f"Attempt {attempt}/{max_attempts} - Type in the guessed number: "))
    except ValueError:
      print("Enter valid number")
      continue

    if not 1<=user_input<=100:
       print("Pick a number between 1 and 100")
       continue

    if user_input == random_num:
      print(f"Congratulations! You guessed correctly in {attempt} attempts. The number is {random_num}")
      break
    elif user_input > random_num:
      print("Wrong!Go lower")
    else:
      print("Wrong!Go higher") 

    attempt += 1
else:
    print(f"Out of attempts. The number is {random_num}")
    

    
