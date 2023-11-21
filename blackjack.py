import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(hand):
    return sum(hand)

def print_player():
    print(f"\tYour cards: {player_hand}, current score: {player_current_score}")


player_hand = [deal_card(), deal_card()]
# player_hand = [11,11]
player_current_score = calculate_score(player_hand)

dealer_hand = [deal_card(), deal_card()]
dealer_current_score = calculate_score(dealer_hand)

print(f"Your cards are: {player_hand}, current score: {player_current_score}")
print(f"Computer's first card: {dealer_hand[0]}")
hit_me = True

if player_current_score == 21 and dealer_current_score == 21:
    print("Dealer and player have Blackjack. Push 😐")
    quit()
elif player_current_score == 21 and dealer_current_score != 21:
    print("Player has Blackjack! Congratulations, you win 🎉")
elif player_current_score != 21 and dealer_current_score == 21:
    print("Dealer has Blackjack, you lose 😭")
else:
    if input("Type 'h' to get another card, type 'p' to pass: ") == "h":
        player_hand.append(deal_card())
        player_current_score = calculate_score(player_hand)
        print_player()
    else:
        keep_dealing = True
        while keep_dealing:
            dealer_hand.append(deal_card())
            dealer_current_score = calculate_score(dealer_hand)
            if dealer_current_score > 21:
                if 11 in dealer_hand:
                    #calculate 11s
                    dealer_hand[dealer_hand.index(11)] = 1
                else:
                    keep_dealing = False
            elif dealer_current_score >= 17:
                keep_dealing = False
    print_player()
    print(f"\tDealer final hand {dealer_hand}, dealer final score: {dealer_current_score}")