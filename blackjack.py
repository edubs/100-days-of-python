import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(player = "user"):
    card = random.choice(cards)
    print(f"\t\t>>> {card} was dealt to {player}")
    return card

def calculate_score(hand):
    return sum(hand)

def print_player():
    print(f"\tYour cards: {player_hand}, current score: {calculate_score(player_hand)}")

def print_dealer():
    print(f"\tDealer's cards: {dealer_hand}, current score: {calculate_score(dealer_hand)}")

def you_lose():
    print(f"\tYou lost! 😭")
    quit()

def determine_winner():
    if calculate_score(player_hand) > calculate_score(dealer_hand):
        print(f"player > {player_hand}, beats > {dealer_hand}")
    elif calculate_score(player_hand) == calculate_score(dealer_hand):
        print(f"it's a tie.")
    else:
        print(f"dealer wins with {dealer_hand}")


def deal_player(hit_me):
    if hit_me == 'h':
        player_hand.append(deal_card())
        player_current_score = calculate_score(player_hand)
        if player_current_score > 21:
            if 11 in player_hand:
                print(f"Converting Ace to a 1 so you don't lose.")
                player_hand[player_hand.index(11)] = 1
                print_player()
            else:
                print_player()
                print(f"\tBUSTED! SOORRY!")
                you_lose()
        print_player()
        deal_player(input("Type 'h' to get another card, type 'p' to pass: "))
    elif hit_me == 'p':
        print(f"\tPassing.")
        dealer_plays()

def dealer_plays():
    dealer_current_score = calculate_score(dealer_hand)
    print_dealer()
    if dealer_current_score < 16:
        dealer_hand.append(deal_card("dealer"))
        dealer_plays()
    elif dealer_current_score > 21:
        print(f"Dealer busts! YOU WIN!!")
    elif dealer_current_score >= 17:
        determine_winner()
    else:
        dealer_plays()

player_hand = [random.choice(cards), random.choice(cards)]
dealer_hand = [random.choice(cards), random.choice(cards)]

print(f"\tYour cards are: {player_hand}, current score: {calculate_score(player_hand)}")
print(f"\tComputer's first card: {dealer_hand[0]}")

if calculate_score(player_hand) == 21 and calculate_score(dealer_hand) == 21:
    print("Dealer and player have Blackjack. Push 😐")
elif calculate_score(player_hand) == 21 and calculate_score(dealer_hand) != 21:
    print("Player has Blackjack! Congratulations, you win 🎉")
elif calculate_score(player_hand) != 21 and calculate_score(dealer_hand) == 21:
    print("Dealer has Blackjack, you lose 😭")
    print_dealer()
else:
    deal_player(input("Type 'h' to get another card, type 'p' to pass: "))
