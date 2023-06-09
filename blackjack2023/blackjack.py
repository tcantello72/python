# Program: Blackjack Game
# Programmer: Toby Cantello
# Created on June 7, 2023
# Last updated on June 8, 2021
# These are improvements made to a basic one person blackjack game I created on May 16, 2021

# ---- Import Section ----
import random
import os

# ---- Functions Section ----

# Function for clearing the console screen at the start of the game
clear = lambda: os.system('cls')

# Function that will return the value of the first two cards dealt to each player and dealer
def FirstTwoCards(player):
    count = 0
    handValue = 0
     
    while count <= 1:
            rnumber = random.randint(0, 51)
            card_name_print = card_name[rnumber]
            card_value_print = card_value[rnumber]
            print (player, "your card is the", card_name_print)
            handValue = handValue + card_value_print
            count = count + 1
    print (player, "your score is ", handValue)
    return handValue

# Function that lets each player choose to Hit or Stand. Player at a time and one card at a time
def HitOrStand (handValue, player):
    while handValue <= 21:
        print()
        print(player, "it's your turn. You currently have ", handValue)
        hit_stand = input("Enter h to Hit or s to Stand:\n")
        if hit_stand == 'h':
            rnumber = random.randint(0, 51)
            card_name_print = card_name[rnumber]
            card_value_print = card_value[rnumber]
            handValue = handValue + card_value_print
            print (player, "your card is the", card_name_print)
            print (player, "your score is ", handValue)
            print()
        elif hit_stand == 's':
            print (player, "stands with a score of", handValue)
            print ()
            return handValue
        if handValue > 21:
            print (player, "you have busted.")
            print ()
            return handValue

# Function that hands the dealer additional cards per the rules of blackjack
def DealerHitOrStand(handValue):
    print()
    print("Dealer's Turn and they currently have ", handValue)
    if handValue <= 17:
        rnumber = random.randint(0, 51)
        card_name_print = card_name[rnumber]
        card_value_print = card_value[rnumber]
        handValue = handValue + card_value_print
        print ("Dealer's card is the", card_name_print)
        print ("Dealer's score is ", handValue)
        print()
    elif  handValue > 17 and handValue <=21:
        print ("Dealer stands with a score of ", handValue)
    elif handValue >21:
        print ("Dealer has busted with a score of ", handValue)
    return handValue

# Function to determine who won (player or dealer) and deal with player bank amount
def WhoWon(player, bankPlayer, betPlayer, playerHandValue, dealerHandValue):
    if playerHandValue <=21 and dealerHandValue <= 21 and playerHandValue > dealerHandValue:
        bankPlayer = bankPlayer + betPlayer
        print(player, "you have beat the Dealer and your new bank value is ", bankPlayer)
        return bankPlayer
    elif playerHandValue <=21 and dealerHandValue <= 21 and playerHandValue < dealerHandValue:
        bankPlayer = bankPlayer - betPlayer
        print(player, "the Dealer beat you and your new bank value is ", bankPlayer)
        return bankPlayer
    elif playerHandValue > 21:
        bankPlayer = bankPlayer - betPlayer
        print(player, "you Busted and your new bank value is ", bankPlayer)
        return bankPlayer
    if playerHandValue <=21 and dealerHandValue > 21:    
        bankPlayer = bankPlayer + betPlayer
        print(player, "you won as the Dealer busted and your new bank value is ", bankPlayer)
        return bankPlayer

    
# List of a desk of playing cards with name and value Section
cardid = {
    '2 of Clubs': 2,
    '3 of Clubs': 3,
    '4 of Clubs': 4,
    '5 of Clubs': 5,
    '6 of Clubs': 6,
    '7 of Clubs': 7,
    '8 of Clubs': 8,
    '9 of Clubs': 9,
    '10 of Clubs': 10,
    'Jack of Clubs': 10,
    'Queen of Clubs': 10,
    'King of Clubs': 10,
    'Ace of Clubs': 11,
    '2 of Spades': 2,
    '3 of Spades': 3,
    '4 of Spades': 4,
    '5 of Spades': 5,
    '6 of Spades': 6,
    '7 of Spades': 7,
    '8 of Spades': 8,
    '9 of Spades': 9,
    '10 of Spades': 10,
    'Jack of Spades': 10,
    'Queen of Spades': 10,
    'King of Spades': 10,
    'Ace of Spades': 11,
    '2 of Hearts': 2,
    '3 of Hearts': 3,
    '4 of Hearts': 4,
    '5 of Hearts': 5,
    '6 of Hearts': 6,
    '7 of Hearts': 7,
    '8 of Hearts': 8,
    '9 of Hearts': 9,
    '10 of Hearts': 10,
    'Jack of Hearts': 10,
    'Queen of Hearts': 10,
    'King of Hearts': 10,
    'Ace of Hearts': 11,
    '2 of Diamonds': 2,
    '3 of Diamonds': 3,
    '4 of Diamonds': 4,
    '5 of Diamonds': 5,
    '6 of Diamonds': 6,
    '7 of Diamonds': 7,
    '8 of Diamonds': 8,
    '9 of Diamonds': 9,
    '10 of Diamonds': 10,
    'Jack of Diamonds': 10,
    'Queen of Diamonds': 10,
    'King of Diamonds': 10,
    'Ace of Diamonds': 11,
}

# ---- MAIN PROGRAM ----
# Starting value of variables
card_name = list(cardid.keys())
card_value = list(cardid.values())
bankPlayer1 = 2500
bankPlayer2 = 2500

# Opening of the game
clear()
print ("Welcome to Toby's Blackjack Game")
print ()
print ("Goal is to get as close to 21 as you can without going over")
print ("ACEs count as 11 points and the  Dealer Stands with 18, 19, 20 amd 21 points")
print ("Each Player will start with $2500 in the bank")
print ()
player1 = input('Player 1 please enter your name: ')
player2 = input('Player 2 please enter your name: ')
print()

# Start of hand
while True:
    print (player1, "your max bet is ",bankPlayer1)
    betPlayer1 = int(input("Please enter how much you would like to wager: "))
    print()
    print (player2, "your max bet is ",bankPlayer2)
    betPlayer2 = int(input("Please enter how much you would like to wager: "))
    print()

    # first two cards of hand
    if betPlayer1 <= bankPlayer1:
        handValuePlayer1 = FirstTwoCards(player1)
        print()
    if betPlayer2 <= bankPlayer2:
        handValuePlayer2 = FirstTwoCards(player2)
        print()
    handValueDealer = FirstTwoCards('Dealer')

    # Hit or Stand
    handValuePlayer1 = HitOrStand(handValuePlayer1, player1)
    handValuePlayer2 = HitOrStand(handValuePlayer2, player2)
    handValueDealer = DealerHitOrStand(handValueDealer)

    # Who wins the player or dealer
    bankPlayer1 = WhoWon(player1, bankPlayer1, betPlayer1, handValuePlayer1, handValueDealer)
    bankPlayer2 = WhoWon(player2, bankPlayer2, betPlayer2, handValuePlayer2, handValueDealer)
    print()


















"""

bankPlayer = bankPlayer + betPlayer

 print (player, "Your new bank value is $", bankPlayer,".")

 print (player, "your new bank value is $",bankPlayer)

        # hit or stand choice
       
        play_again = input("Would you like to play again? y or n \n")
        count = 0
        while play_again.lower() not in ("y","n"):
            play_again = input("Would you like to play again? y or n \n")
        if play_again == "n":
            break
print ("Thanks for Playing")
"""