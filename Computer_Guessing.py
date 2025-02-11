import random as rdm

x = int(input('Maximum Number?: '))

def Computer_Guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = rdm.randint(low, high)
        else:
            guess = low or high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'The Computer guessed your number, {guess}, correctly!')

Computer_Guess(x)