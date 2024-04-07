import random
import math

# Taking user inputs for lower and upper bounds
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# Generating a random number within the specified range
random_number = random.randint(lower, upper)

# Calculating the maximum number of guesses based on the range
max_guesses = round(math.log(upper - lower + 1, 2))
print("\nYou have only", max_guesses, "chances to guess the integer!\n")

# Initializing the number of guesses
guess_count = 0

# Looping until the maximum number of guesses is reached
while guess_count < max_guesses:
    guess_count += 1

    # Taking user input for the guess
    guess = int(input("Guess a number:- "))

    # Checking if the guess matches the random number
    if guess == random_number:
        print("Congratulations! You guessed it in", guess_count, "tries.")
        break
    elif guess < random_number:
        print("You guessed too small!")
    else:
        print("You guessed too high!")

# If the maximum number of guesses is reached without guessing the number
if guess_count >= max_guesses:
    print("\nThe number is", random_number)
    print("Better Luck Next time!")
