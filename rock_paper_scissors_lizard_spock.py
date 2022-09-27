import numpy as np
import pandas as pd

import random

def play():
    user = input('Let\'s play Rock, Paper, Scissors, Lizard, Spock!\nWhat\'s your choice?\n     [R] for Rock, [P] for Paper, [S] for Scissors, [L] for Lizard, [K] for Spock\n').upper()
    computer = random.choice(['R', 'P', 'S', 'L', 'K'])
    print(f'Computer plays {computer}.\n')
    if user == computer:
        return 'It\'s a tie. You both live to fight another day...'
    if is_win(user, computer):
        return 'You win!'
    return 'FATALITY\nYou lose.'

def is_win(player, opponent):
    # return true if player wins
    # R > S, L
    # P > R, K
    # S > P, L
    # L > P, K
    # K > R, S
    if (player == 'R' and opponent in ['S', 'L'])\
            or (player == 'P' and opponent in ['R', 'K'])\
            or (player == 'S' and opponent in ['P', 'L'])\
            or (player == 'L' and opponent in ['P', 'K'])\
            or (player == 'K' and opponent in ['R', 'S']):
        return True

print(play())
