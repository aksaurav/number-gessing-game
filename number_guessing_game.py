
import random
import time

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        # getting user input
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # setting up the conditons
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    # exiting the loop
    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
    time.sleep(.8)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
    time.sleep(.8)

while 1:
    print("*****Number Gussing Game******")
    print("1. Guess computer number")
    print("2. Computer guess your number")
    print("3. Exit")

    choice = input("Enter you choice: ")
    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            x = input("Enter a maxmum number you want to guess: ")
            if x.isdigit():
                x = int(x)
                guess(x)
            else:
                print("Enter a number")
        elif choice == 2:
                computer_guess(10)
        elif choice == 3:
            break
        else:
            print("Invalid Choice!")
        time.sleep(.8)
    else:
        print('Provided value is not a number, is a negative number or a float')
