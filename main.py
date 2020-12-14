############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import art
import random

def score(cards):
    cards_score = 0
    for x in cards:
        cards_score += x
    return(cards_score)

def card_pick(deck):
    deck.append(random.choice(cards))

def print_score(deck):
    print(f"Your cards: {player_cards}, current score: {score(player_cards)}")
    print(f"Computer's first card: {computer_cards[1]}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play == "y":
    print(art.logo)

while play == "y":
    player_cards = []
    computer_cards = []
    card_pick(player_cards)
    card_pick(player_cards)
    while score(computer_cards) < 17:
        card_pick(computer_cards)
        
    print_score(player_cards)
    
    def redeal():
        deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal == "y":
            card_pick(player_cards)
            print_score(player_cards)
            if score(player_cards) > 21:
                print_score(player_cards)
                print_score(computer_cards)
                print("You went over. You lose.")
            else:
                redeal()
    
    redeal()
    print_score(player_cards)
    print_score(computer_cards)

    if score(computer_cards) > 21:
        print("You win.")
    elif score(player_cards) > score(computer_cards):
        print("You win.")
    else:
        print("You lose")
    
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    
# Still pending