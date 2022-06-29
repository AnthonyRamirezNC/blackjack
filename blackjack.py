from deck_of_cards import deck_of_cards

def starting_shuffle():
    player_deck = []
    dealer_deck = []
    deck = deck_of_cards.DeckOfCards()
    deck.order_deck()
    for card_count in range(0,2, 1):
        dealer_card = deck.give_random_card().name
        dealer_deck.append(dealer_card)
        #print(f'Dealers card is {dealer_card}')
        player_card = deck.give_random_card().name
        player_deck.append(player_card)
        #print(f'Players card is {player_card}')
    return player_deck, dealer_deck, deck
    
def check_split(player_deck):
    if player_deck[0] == player_deck[1]:
        return True
    else:
        return False



def main():
    player_deck, dealer_deck, deck = starting_shuffle()
    print(player_deck)
    canSplit = check_split(player_deck)
    Quit = False
    Busted = False
    Standing = False
    while Quit == False and Busted == False and Standing == False:
        if canSplit == True:
            choice = input('What will you do? 1: Hit 2: Stand 3: Double Down 4: Split Q: Quit\ntype or give number: ')
        elif canSplit == False:
            choice = input('What will you do? 1: Hit 2: Stand 3: Double Down Q: Quit\ntype or give number: ')
        if choice == '1':
            print('hitting')
        elif choice == '2':
            print('standing')
        elif choice == '3':
            print('Doubling Down')
        elif(choice == '4' and canSplit == True) or (choice == 'Split' and canSplit == True) or (choice == 'split' and canSplit == True):
            print('splitting')
        elif(choice == '4' and canSplit == False) or (choice == 'Split' and canSplit == False) or (choice == 'split' and canSplit == False):
            print('Cannot Split')
        elif choice == 'q' or choice == 'Q':
            print('Quitting')
        else:
            print('Invalid choice')
    print('continue')
            


main()