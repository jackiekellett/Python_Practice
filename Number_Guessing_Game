import numpy as np
import pandas as pd

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess an integer between 1 and {x}: \n'))
        if 1 <= guess <= 10:
            if guess < random_number:
                print('Try again. You were too low.')
            elif guess > random_number:
                print('Guess again. You were too high.')
        else:
            print(f"Really? {guess} isn't between 1 and {x}. Duh. Try again.")
    print(f"Congrats! {random_number} is correct!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high
        feedback = input(f"Is {guess} too high [H], too low [L], or correct [C]?\n").upper()
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        elif feedback not in ['H', 'L', 'C']:
            print(f"{feedback} isn't a valid option. Don't cheat.")
    print(f"Yay! I guessed your number, {guess}, correctly!")

# guess(10)

computer_guess(1000)
