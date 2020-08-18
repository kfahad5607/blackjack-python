import random
import time

deck = [{'suit': 'spades', 'type': 'ace', 'value': 11}, {'suit': 'spades', 'type': '2', 'value': 2}, {'suit': 'spades', 'type': '3', 'value': 3}, {'suit': 'spades', 'type': '4', 'value': 4}, {'suit': 'spades', 'type': '5', 'value': 5}, {'suit': 'spades', 'type': '6', 'value': 6}, {'suit': 'spades', 'type': '7', 'value': 7}, {'suit': 'spades', 'type': '8', 'value': 8}, {'suit': 'spades', 'type': '9', 'value': 9}, {'suit': 'spades', 'type': '10', 'value': 10}, {'suit': 'spades', 'type': 'king', 'value': 10}, {'suit': 'spades', 'type': 'queen', 'value': 10}, {'suit': 'spades', 'type': 'jack', 'value': 10}, {'suit': 'hearts', 'type': 'ace', 'value': 11}, {'suit': 'hearts', 'type': '2', 'value': 2}, {'suit': 'hearts', 'type': '3', 'value': 3}, {'suit': 'hearts', 'type': '4', 'value': 4}, {'suit': 'hearts', 'type': '5', 'value': 5}, {'suit': 'hearts', 'type': '6', 'value': 6}, {'suit': 'hearts', 'type': '7', 'value': 7}, {'suit': 'hearts', 'type': '8', 'value': 8}, {'suit': 'hearts', 'type': '9', 'value': 9}, {'suit': 'hearts', 'type': '10', 'value': 10}, {'suit': 'hearts', 'type': 'king', 'value': 10}, {'suit': 'hearts', 'type': 'queen', 'value': 10}, {'suit': 'hearts', 'type': 'jack', 'value': 10}, {
    'suit': 'diamonds', 'type': 'ace', 'value': 11}, {'suit': 'diamonds', 'type': '2', 'value': 2}, {'suit': 'diamonds', 'type': '3', 'value': 3}, {'suit': 'diamonds', 'type': '4', 'value': 4}, {'suit': 'diamonds', 'type': '5', 'value': 5}, {'suit': 'diamonds', 'type': '6', 'value': 6}, {'suit': 'diamonds', 'type': '7', 'value': 7}, {'suit': 'diamonds', 'type': '8', 'value': 8}, {'suit': 'diamonds', 'type': '9', 'value': 9}, {'suit': 'diamonds', 'type': '10', 'value': 10}, {'suit': 'diamonds', 'type': 'king', 'value': 10}, {'suit': 'diamonds', 'type': 'queen', 'value': 10}, {'suit': 'diamonds', 'type': 'jack', 'value': 10}, {'suit': 'clubs', 'type': 'ace', 'value': 11}, {'suit': 'clubs', 'type': '2', 'value': 2}, {'suit': 'clubs', 'type': '3', 'value': 3}, {'suit': 'clubs', 'type': '4', 'value': 4}, {'suit': 'clubs', 'type': '5', 'value': 5}, {'suit': 'clubs', 'type': '6', 'value': 6}, {'suit': 'clubs', 'type': '7', 'value': 7}, {'suit': 'clubs', 'type': '8', 'value': 8}, {'suit': 'clubs', 'type': '9', 'value': 9}, {'suit': 'clubs', 'type': '10', 'value': 10}, {'suit': 'clubs', 'type': 'king', 'value': 10}, {'suit': 'clubs', 'type': 'queen', 'value': 10}, {'suit': 'clubs', 'type': 'jack', 'value': 10}]

lastId = 1
currentHand = 1
allHands = []
splitIndex = set()
print('Enter the amount of bet...')
bet = int(input())
bet = 100

dealer = {'cards': [], 'totalScore': 0}
player = {'id': 1, 'cards': [], 'totalScore': 0,
          'splitHandCards': [], 'isStand': False , 'betWon': None}
# player1 = {'id': 1, 'cards': [{'suit': 'hearts', 'type': '9', 'value': 9}, {'suit': 'spades', 'type': '9', 'value': 9}], 'totalScore': 0, 'splitHandCards': [], 'isStand': False, 'betWon': None}
allHands.append(player)


def createNewHand(card):
    global lastId
    user = {'id': lastId + 1, 'cards': [], 'totalScore': 0,'splitHandCards': [],
            'isStand': False, 'betWon': None}
    user['cards'].append(card)
    lastId += 1
    return user

# Hit : take a random card from the shuffle
def hit(user):
    card = random.choice(deck)
    deck.remove(card)
    user['cards'].append(card)
    return card

def displayCards():
    global currentHand
    dealerLength= len(dealer['cards'])
    print('Dealer\'s card is:')
    print(f"{dealer['cards'][dealerLength - 1]['type']} of {dealer['cards'][dealerLength - 1]['suit']} with value of {dealer['cards'][dealerLength - 1]['value']} \n")
    print(f"Cards in hand {currentHand}:")
    for card in allHands[0]['cards']:
        print(f"{card['type']} of {card['suit']} with value of {card['value']} ")

def calculateScore(user):
    score = 0
    for card in user['cards']:
        score += card['value']
    user.update({'totalScore': score})
    return score

def removeHand():
    global currentHand
    currentHand +=1
    allHands.pop(0)
    if len(allHands) == 0:
        exit()

def dealerCards():
    print('Dealer\'s Cards are:')
    for card in dealer['cards']:
        print(f"{card['type']} of {card['suit']} with value of {card['value']}.")
    print('')

def checkWinner(player, dealer):
    if calculateScore(player) > 21:
        player.update({'betWon': 0})
        dealerCards()
        print(f'You got busted with the score of {calculateScore(player)} and lost the bet of {bet}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif calculateScore(dealer) > 21:
        player.update({ 'betWon' : bet})
        dealerCards()
        print(f'Dealer got busted with the score of {calculateScore(dealer)} and you have won {bet}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif calculateScore(player) == 21:
        player.update({ 'betWon' : (bet*1.5)})
        dealerCards()
        print(f'You got the blackjack and you won {bet*1.5}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif calculateScore(dealer) == 21:
        player.update({ 'betWon' : 0})
        dealerCards()
        print(f'Dealer got the blackjack and you lost the bet of {bet}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif (calculateScore(dealer) == calculateScore(player)) and (player['isStand'] == True):
        player.update({ 'betWon' : None})
        dealerCards()
        print(f'Game is pushed as both dealer and player got the score of {calculateScore(dealer)}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif (calculateScore(dealer) > calculateScore(player)) and (player['isStand'] == True):
        player.update({ 'betWon' : 0})
        dealerCards()
        print(
            f'You have lost the bet of {bet} as your score is {calculateScore(player)} and dealer\'s score is {calculateScore(dealer)}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

    elif (calculateScore(dealer) < calculateScore(player)) and (player['isStand'] == True):
        player.update({ 'betWon' : bet})
        dealerCards()
        print(
            f'You have won {bet} as your score is {calculateScore(player)} and dealer\'s score is {calculateScore(dealer)}.\n')
        removeHand()
        displayCards()
        print(f'Your score is {calculateScore(allHands[0])}.\n')
        return

def split(player):
    if len(player['cards']) == 2:
        for card in player['cards']:
            for i in range(len(player['cards'])):
                if (card['value'] == player['cards'][i]['value']) and (i != player['cards'].index(card)):
                    splitIndex.add(i)
        if len(splitIndex) > 0:
            for index in splitIndex:
                player['splitHandCards'].append(player['cards'][index])
                card = player['cards'][index]
                allHands.append(createNewHand(card))
            splitIndex.clear()

            for card in allHands[allHands.index(player)]['cards']:
                if card in player['splitHandCards']:
                    allHands[allHands.index(player)]['cards'].remove(card)
                    player['splitHandCards'].remove(card)
            allHands.pop(0)
        elif len(splitIndex) == 0:
            print('Cannot split the hands as values of the cards are not equal.')
    else:
        print('Cannot Split!')

def surrender():
    print(f'You chose to surrender and lost {bet/2}.\n')
    removeHand()

if __name__ == "__main__":
    print("1. Start \t 2. Exit")
    
    ch = int(input())

    while ch != 2:
        if ch == 1:
            hit(player)
            hit(player)
            while calculateScore(dealer) < 17:
                hit(dealer)

            
            while True:
                print('-------------Displaying Cards---------------\n')
                displayCards()
                print(f'Your score is {calculateScore(allHands[0])}\n')
                checkWinner(allHands[0], dealer)

                # user choices
                print('1. Hit')
                print('2. Stand')
                print('3. Split')
                print('4. Surrender')

                user_choice = int(input())

                if user_choice == 1:
                    print('Drawing a Card for you....\n')
                    time.sleep(1)
                    hit(allHands[0])
                elif user_choice == 2:
                    allHands[0].update({'isStand': True})
                elif user_choice == 3:
                    split(allHands[0])
                elif user_choice == 4:
                    surrender()
                else:
                    print('Unexpected input')
        elif ch == 2:
            exit()
        else:
            print('Wrong Choice! Try Again')
        print("\nTo Play Again enter   1. Start \t 2. Exit")
        ch = int(input())

        # Resetting global variables 
        lastId = 1
        currentHand = 1
        allHands = []
        splitIndex = set()
        dealer = {'cards': [], 'totalScore': 0}
        player = {'id': 1, 'cards': [], 'totalScore': 0,'splitHandCards': [], 'isStand': False, 'betWon': None}
        allHands.append(player)

