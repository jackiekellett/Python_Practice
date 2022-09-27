import random

class Choice:
    def __init__(self, name, ab, ftw):
        self.name = name
        self.abbrev = ab
        self.beats = ftw

c1 = Choice('Rock', 'R', ['S', 'L'])
c2 = Choice('Paper', 'P', ['R', 'K'])
c3 = Choice('Scissors', 'S', ['P', 'L'])
c4 = Choice('Lizard', 'L', ['P', 'K'])
c5 = Choice('Spock', 'K', ['R', 'S'])

options = [c1.abbrev, c2.abbrev, c3.abbrev, c4.abbrev, c5.abbrev]

def play():
    user = input(f'Let\'s play {c1.name}, {c2.name}, {c3.name}, {c4.name}, {c5.name}!\nWhat\'s your choice?\n     [{c1.abbrev}] for {c1.name}, [{c2.abbrev}] for {c2.name}, [{c3.abbrev}] for {c3.name}, [{c4.abbrev}] for {c4.name}, [{c5.abbrev}] for {c5.name}\n').upper()
    computer = random.choice(options)
    print(f'Computer plays {computer}.\n')
    if user == computer:
        return 'It\'s a tie. You both live to fight another day...'
    if is_win(user, computer):
        return 'You win!'
    return 'FATALITY\nYou lose.'

def is_win(player, opponent):
    if (player == c1.abbrev and opponent in c1.beats)\
            or (player == c2.abbrev and opponent in c2.beats)\
            or (player == c3.abbrev and opponent in c3.beats)\
            or (player == c4.abbrev and opponent in c4.beats)\
            or (player == c5.abbrev and opponent in c5.beats):
        return True
    else:
        return False

print(play())
