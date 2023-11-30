import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")
the_number = random.randint(1, 100)
print(f"the number is: {the_number}")
play_the_game = True

# set attempts based on difficulty
if difficulty == "hard":
    num_guesses = 5
else:
    num_guesses = 10

while play_the_game:
    print(f"You have {num_guesses} attempts remaining to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess == the_number:
        print(f"You got it! The answer was {the_number}")
        play_the_game = False
    elif user_guess > the_number:
        print("Too high.")
        print("Guess again.")
        num_guesses-=1
    else:
        print("Too low.")
        print("Guess again.")
        num_guesses-=1

    if num_guesses == 0:
        print("You've run out of guesses, you lose.")
        play_the_game = False