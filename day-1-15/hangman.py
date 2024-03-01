import random


word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives_left = 6

# Testing code
# print(f"psssst. the solution is {chosen_word}")

guesses = []
display = []
for x in chosen_word:
    display.append("_")

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"You've already guessed the letter '{guess}', guess another letter.\n")
        print(f"guesses remaining: {lives_left}\n")
    elif guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                display[index] = letter
        guesses.append(guess)
    elif guess not in chosen_word:
        print(f"{guess} is WRONG.\n")
        lives_left-=1
        guesses.append(guess)
        print(f"guesses remaining: {lives_left}\n")

    if lives_left == 0:
        print("YOU LOSE.")
        break

    print(display)
print("Congratulations, you won!")