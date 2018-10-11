import random

random_choice = random.randint(0,2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
elif random_choice == 2:
    computer_choice = 'scissors'

print ('The computer chooses', computer_choice)
