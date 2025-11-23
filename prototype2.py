import random
#making the deck of cards
    
deck_suits = ["♠","♥","♣","♦"]    

deck_values = ["2","3","4","5","6","7","8","9","10",
          "J","Q","K","A"]
deck =[]
for key in deck_values:
    for suit in deck_suits:
        deck.append({"value":key,"suit":suit, "rank":values_rank[key]})
#shuffle deck

random.shuffle(deck)

#player draws 2 cards

player_draws = 2

player_cards = []

print("Your cards are: ")
while player_draws > 0:
    player_card = deck.pop()
    player_cards.append(player_card)
    player_draws = player_draws - 1

print(player_cards)

#dealer draws 3 cards 

dealer_draws = 5

dealer_cards = []

print("dealer cards are: ")
while dealer_draws > 2:
    dealer_card = deck.pop()
    dealer_cards.append(dealer_card)
    dealer_draws = dealer_draws - 1
    
print(dealer_cards)    

#flop
while dealer_draws > 0:
    print(f"{dealer_draws} draws remaining")
    ask_draw_again = input("do you wish to draw again? [y/n]\n")
    if ask_draw_again == "y":
        dealer_card = deck.pop()
        dealer_cards.append(dealer_card)
        dealer_draws = dealer_draws - 1
    else:
        print(f"Your cards are\n{player_cards}")
        print(f"Dealer cards are\n{dealer_cards}")
        break
    print(f"Your cards are\n{player_cards}")
    print(f"Dealer cards are\n{dealer_cards}")

#now we have player and dealer cards, figure out hands

#make player and dealer cards into one big list of dictionaires

final_cards = player_cards + dealer_cards


