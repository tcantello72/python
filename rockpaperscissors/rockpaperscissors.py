# Written by Toby Cantello
# Created on 6/1/23
# Last updated on 6/1/23


# ----Import Section----
import random

# ----Functions Section----
# Function for computer to select which option to play
def computerSelection():
    number = random.randint(1, 3)

    if number == 1:
        computerHand = 'Rock'
        return computerHand
    elif number == 2:
        computerHand = 'Paper'
        return computerHand
    elif number == 3:
        computerHand = 'Scissors'
        return computerHand

# Function for computer to select which option to play
def playerSelection():
    playerInput = int(input('Please select: 1 for Rock, 2 for Paper or 3 for Scissors: '))
    print("")

    if playerInput == 1:
        playerHand = 'Rock'
        return playerHand
    elif playerInput == 2:
        playerHand = 'Paper'
        return playerHand
    elif playerInput == 3:
        playerHand = 'Scissors'
        return playerHand

# Function for hand to be played
def playHand(player, computer):
    print('Player -', player)
    print('Computer -', computer)

    winner = ''

    if ((player == 'Rock') and (computer == 'Rock')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Rock') and (computer == 'Paper')):
        print('Computer Wins!')
        winner = 'computer'
        return winner
    elif ((player == 'Rock') and (computer == 'Scissors')):
        print('Player Wins!')
        winner = 'player'
        return winner
    
    if ((player == 'Paper') and (computer == 'Paper')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Paper') and (computer == 'Rock')):
        print('Player Wins!')
        winner = 'player'
        return winner
    elif ((player == 'Paper') and (computer == 'Scissors')):
        print('Computer Wins!')
        winner = 'computer'
        return winner
    
    if ((player == 'Scissors') and (computer == 'Scissors')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Scissors') and (computer == 'Paper')):
        print('Player Wins!')
        winner = 'player'
        return winner
    elif ((player == 'Scissors') and (computer == 'Rock')):
        print('Computer Wins!')
        winner = 'computer'
        return winner


# ----Game play starts here----

# Global variables
playerScore = 0
computerScore = 0
ties = 0
playAgain = 'y'

# The Game
while playAgain == 'y':

    winner = playHand(playerSelection(), computerSelection())

    if winner == 'tie':
        playerScore == playerScore
        computerScore == computerScore
        ties = ties + 1
    elif winner == 'player':
        playerScore = playerScore + 1
        computerScore == computerScore
        ties==ties
    elif winner == 'computer':
        playerScore = playerScore
        computerScore = computerScore + 1
        ties==ties

    print("")
    print('Player Score -', playerScore)
    print('Computer Score -', computerScore)
    print('Ties -', ties)
    print("")
    playAgain = input('Would you like to play again? (y or n) ')
    print("")
    if playAgain == 'n':
        print('Thanks for Playing')
        print('')
        if playerScore > computerScore:
            print('PLAYER WINS!', playerScore, "to", computerScore)
            print('')
        elif computerScore > playerScore:
            print('COMPUTER WINS!', computerScore, "to", playerScore)
            print('')
        else:
            print('Game ends in a Tie!', playerScore, "to", computerScore)
        quit()