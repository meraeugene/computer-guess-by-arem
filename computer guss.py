import random

print("The computer will guess your desired number, pick a random number between 1-1000")
print()

def computer_guess(x):
    low = 1
    high = x 
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low,high)
        feedback= input(f"Is {guess} too high(h),too low(l), or correct(c)? ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed your number {guess}")

computer_guess(1000)
