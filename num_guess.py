#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct. 5, 2022
# Number guessing program, change constants.py correct_answer to have the correct answer you want
import constants


def main():

    # Spacer
    print("")

    # Obtain user guess for the correct answer
    print("This is a number guessing game, choose a number between 1-10")
    guess_answer = int(input("Insert your guess (1 - 10): "))

    # Spacer
    print("")

    # Answer checking, seeing if user input is correct
    if guess_answer == constants.correct_answer:
        print("Your guess is correct")

    else:
        print("Your answer is incorrect")


if "__main__" == __name__:
    main()
