from deck_of_cards import deck_of_cards
import numpy as np
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

def hit(player_deck,dealer_deck,deck):
    print('hitting')
    player_deck.append('Ace of Spades')



def player_points(player_deck,ace_over,Busted,points):
    ace_count = 0
    numbers = []
    for card in player_deck:
        for word in card.split():
            if word.isdigit():
                numbers.append(int(word))
                points += int(word)       
        if 'Queen' in card or 'King' in card or 'Jack' in card:
            points += 10
            test = 10
        elif 'Ace ' in card:
            points += 11
            ace_count += 1
        if points > 21 and ace_over == True:
            print('busted')
            Busted = True
            return Busted
        
    if points > 21 and ace_count > 0 and ace_over == False:
        points -= 10
        ace_over = True

    print(points)
    return numbers, ace_count, Busted, ace_over



def main():
    player_deck, dealer_deck, deck = starting_shuffle()
    print(player_deck)
    canSplit = check_split(player_deck)
    Quit = False
    Busted = False
    Standing = False
    ace_over = False
    points = 0
    numbers, ace_count, Busted, ace_over = player_points(player_deck,ace_over,Busted,points)
    print(numbers)
    player_turn = True
    while Quit == False and Busted == False and Standing == False:
        if canSplit == True:
            temp = input('What will you do? 1: Hit 2: Stand 3: Double Down 4: Split Q: Quit\ntype or give number: ')
            choice = temp.lower()

        elif canSplit == False:
            temp = input('What will you do? 1: Hit 2: Stand 3: Double Down Q: Quit\ntype or give number: ')
            choice = temp.lower()

        if choice == '1' or choice == 'hit':
            #run hit function
            if player_turn == True:
                print('players turn')
                new_player_deck = hit(player_deck, dealer_deck, deck)
                player_points(new_player_deck,ace_over,Busted,points)
                player_turn = False

            elif player_turn == False:
                print('dealers turn')
                new_dealer_deck = hit(player_deck, dealer_deck, deck)
                player_points(new_dealer_deck,ace_over,Busted,points)
                player_turn = True

        elif choice == '2' or choice == 'stand':
            print('standing')
            #run stand funtion


        elif(choice == '3') or (choice == 'double down'):
            print('Doubling Down')
            #run doubling down function


        elif(choice == '4' and canSplit == True) or (choice == 'split' and canSplit == True):
            print('splitting')
            #run splitting function

        elif(choice == '4' and canSplit == False) or (choice == 'split' and canSplit == False):
            print('Cannot Split')

        elif choice == 'q' or choice == 'quit':
            print('Quitting')
            Quit = True
        else:
            print('Invalid choice')
    print('game done')


main()