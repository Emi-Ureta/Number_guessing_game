import random
from termcolor import cprint

top_range = input("Type a number greater than 10: ")

if top_range.isdigit():
    top_range = int(top_range)

    while int(top_range) <= 10:
        print("Please type a number greater than 10")
        top_range = input("Type a number greater than 10: ")

else:
    while top_range.isdigit() != True:
        print("Please type a number ")
        top_range = input("Type a number greater than 10: ")

random_number = random.randint(1, int(top_range))
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make your guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue
        
    if user_guess == random_number:
        cprint("You got it right!", 'green')
        break
    elif user_guess < random_number:
        cprint("You were below the number", 'red')
    else:
        cprint("You were above the number", 'red')


print(f"You got it in {guesses} guesses :)")