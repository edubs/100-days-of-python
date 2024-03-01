import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Takes a list of cards and returns the sum of that list."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        print(f"Converting Ace to a 1 so you don't lose.")
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw 😐"
    elif dealer_score == 0:
        return "Dealer wins with Blackjack 🤯"
    elif player_score == 0:
        return "Player wins with Blackjack 😎"
    elif dealer_score > 21:
        return "Dealer went over, player wins 🥳"
    elif player_score > 21:
        return "Player went over, dealer wins 😩"
    elif player_score > dealer_score:
        return "You win 🤫"
    else:
        return "Player loses 😰"

def play_game():
    player_cards = []
    dealer_cards = []
    is_game_over= False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Dealer's first card: {dealer_cards[0]}")


        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'h' to get another card, type 'p' to pass: ")
            if user_should_deal == "h":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Dealers final hand: {dealer_cards}, final score {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
