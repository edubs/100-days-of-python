import random
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    }
]


# get random entry from game data list
def select_entry():
    # TODO: needs to not select a choice that has already been provided
    return random.choice(data)


def print_game_screen(a, b):
    print(f"\n-----| HIGHER |----\n\t----| LOWER |----\n")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(f"\n\tVS.\n")
    print(f"Agaisnt B: {b['name']}, a {a['description']}, from {a['country']}:")


user_score = 0
guess_right = True
working_list = []
working_list.append(select_entry())
working_list.append(select_entry())


while guess_right:
    print_game_screen(working_list[0], working_list[1])
    user_choice = working_list[int(input("Who has more followers? Type '0' or '1': "))]
    working_list.pop(working_list.index(user_choice))

    if user_choice["follower_count"] > working_list[0]["follower_count"]:
        print(f"That's correct!")
        working_list.append(select_entry())
        user_score += 1
    else:
        print(f"Sorry, that's wrong.")
        guess_right = False