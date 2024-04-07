# Number-guessing-game

Number Guessing Game
This project implements a number guessing game where the user selects a range, and the system generates a random integer within that range. The user has to guess the integer in the minimum number of attempts.

Project Overview

The task involves building a number guessing game with the following steps:

User inputs the lower and upper bounds of the range.
The system generates a random integer within the specified range.
The user guesses the integer, and the system provides feedback ("too high" or "too low").
The user continues guessing until they guess the integer correctly or reach the maximum number of guesses.
<b>Analysis<b>
The game implements an efficient guessing strategy to minimize the number of guesses required to find the integer. It intelligently reduces the guessing range based on user feedback, ultimately leading to a successful guess.

Example Scenarios:
User selects a range from 1 to 100. The system randomly selects 42 as the integer. The user successfully guesses the number in 7 attempts.
User selects a range from 1 to 50. The system randomly selects 42 as the integer. The user successfully guesses the number in 6 attempts.
The minimum number of guesses depends on the range, calculated using the formula:


Algorithm
User inputs the lower and upper bounds of the range.
The system generates a random integer within the range.
The user enters their guess in each iteration.
The system provides feedback based on whether the guess is too high or too low.
The user continues guessing until they guess the integer correctly or reach the maximum number of guesses.

Usage
Python: Run the number_guessing_game.py script.


License
This project is licensed under the MIT License. See the LICENSE file for details.

