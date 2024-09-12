# Guessing_game
## Number Guessing Game
## Project Overview
This is simple Python console-based game where the player has to guess a random number between 1 and 10. The program provides a feedback based on player's input and keeps promting the player until the correct number is guessed. This project was created to demonstrate basic Python progrmming skills including input handling,conditional statements, loops, and exception handling.
## Features
1. Random Number Generation: The program generates a random number between 1 and 10 each time it runs.
2. User Input Validation : The game checks if the user's input is valid number between 1 and 10.
3. Error Handling: The game handles cases where the user input non - numerical character, prompting the user to entera valid number.
# Code Explanation: Improved Number Guessing Game
## Purpose:
This Python script is a number guessing game where the user tries to guess a randomly generated number between 1 and 10.

## Breakdown:

Import Necessary Library:

~~~python
import random
~~~

random is imported to generate random numbers.
Generate a Random Number:

~~~python
answer = random.randint(1, 10)
~~~

A random integer between 1 and 10 is generated and stored in the answer variable.
Start the Game Loop:

~~~python
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if 0 < guess <= 11:
            if guess == answer:
                print("You're right!")
                break
            else:
                print("Hey! Try guessing a number > or < 11")
        else:
            print("Please enter a number between 1 and 10")
    except ValueError:
        print("Please enter a number")
~~~

The while True: loop creates an infinite loop until the user guesses correctly or breaks out.
The try-except block handles potential errors:
If the user enters a valid integer within the range (1-10), the if statements check if the guess is correct or incorrect.
If the user enters a number outside the range or a non-numeric value, a ValueError is raised and caught by the except block, prompting the user to enter a valid number.
The break statement exits the loop if the user guesses correctly.
## How it Works:

The script generates a random number.
The user is prompted to guess a number.
The guess is checked against the random number.
If the guess is correct, the game ends.
If the guess is incorrect, the user is prompted to try again.
The loop continues until the user guesses correctly or encounters an invalid input.
## Improvements:

1. Clearer Prompts: The prompts are more informative and provide better guidance to the user.
2. Error Handling: The try-except block ensures that the program doesn't crash if the user enters invalid input.
3. Range Check: The code now checks if the guess is within the valid range of 1 to 10.
4. Consistent Formatting: The code is formatted consistently for better readability.

This improved version of the number guessing game provides a more user-friendly and robust experience.
