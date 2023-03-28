# Number Guessing Game

This is a simple number guessing game where the computer chooses a random number between 1 and 20 and the player has 6 attempts to guess the number correctly.
#How to Play

    1-Run the script in a Python environment.
    2-Enter your name when prompted.
    3-The computer will choose a random number between 1 and 20.
    4:You have 6 attempts to guess the number correctly.
    5-Enter your guess when prompted.
    The computer will provide feedback on whether your guess was too high or too low.
    If you guess the number correctly within 6 attempts, you win the game. Otherwise, you lose.

# Code Explanation

The code starts by importing the random module, which is used to generate a random number between 1 and 20.

The player's name is requested and stored in the myName variable.

A random number is generated using the random.randint() function and stored in the number variable.

The game loop starts, where the player is prompted to enter their guess and provided feedback on whether the guess was too high or too low.

If the player guesses the number correctly within 6 attempts, the loop breaks and a congratulatory message is displayed.

If the player is unable to guess the number within 6 attempts, a message is displayed showing the correct number.
