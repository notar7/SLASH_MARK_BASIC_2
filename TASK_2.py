import random
import time

num = random.randint(1, 100)

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    print("Welcome To Number Guessing Game!!")
    print("You Have Total 5 Chances to guess the Number Between 1-100")

    num_of_guesses = 0
    max_guesses = 5
    while num_of_guesses < max_guesses:
        guesses_remaining = max_guesses - (num_of_guesses+1)
        time.sleep(.25)
        try:
            guess = int(input("Guess the Number : "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if not 1 <= guess <= 100:
            print("The Guessed Number is Out of the Range....!!!\nPlease Enter the Number Between 1-100.")
            continue

        num_of_guesses += 1
        if guess == num:
            break
        elif guess < num:
            print("Number is too small, Guess Again")
        else:
            print("Number is too Big, Guess Again")

        print("Guesses remaining:", guesses_remaining)

    if guess == num:
        print("Great!!! Your Guess was accurate...You guessed the number in ", num_of_guesses, "guesses!!!")
    else:
        print("Sorry, The number was : ", num)

    print("Do you want to play again?")
    playagain = input()
