import random as rdm

x = int(input('Maximum Number?: '))

def Guess(x):
    random_number = rdm.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry guess again. Too high.')
    print(f'Congratulations, You have guessed the number {random_number} correctly!')

Guess(x)