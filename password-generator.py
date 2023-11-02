import random


# letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
# print(letters)

letters  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '=', '?']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the password generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_sybomls=int(input("How many symbols would you like in your password?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))
random_characters=[]
for i in range(nr_letters):
    random_characters.append(random.choice(letters))
for x in range(nr_sybomls):
    random_characters.append(random.choice(symbols))
for x in range(nr_numbers):
    random_characters.append(random.choice(numbers))
random.shuffle(random_characters)
print(f"Your new password is: {''.join(random_characters)} ")
