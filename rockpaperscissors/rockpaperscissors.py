# Written by Toby Cantello
# Created on 6/1/23
# Last updated on 6/2/23


# ----Import Section----
import random

# ----Functions Section----
# Function for computer to select which option to play
def computerSelection():
    number = random.randint(1, 5)

    if number == 1:
        computerHand = 'Rock'
        return computerHand
    elif number == 2:
        computerHand = 'Paper'
        return computerHand
    elif number == 3:
        computerHand = 'Scissors'
        return computerHand
    elif number == 4:
        computerHand = 'Lizard'
        return computerHand
    elif number == 5:
        computerHand = 'Spock'
        return computerHand

# Function for computer to select which option to play
def playerSelection():
    playerInput = int(input('Please select: 1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard or 5 for Spock: '))
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
    elif playerInput == 4:
        playerHand = 'Lizard'
        return playerHand
    elif playerInput == 5:
        playerHand = 'Spock'
        return playerHand
    elif playerInput > 5:
        print('Please enter an integer between 1 and 5')
        playerHand = playerSelection()
        return playerHand

# Function for hand to be played
def playHand(player, computer):
    print('Player -', player)
    print('Computer -', computer)

    winner = ''

    # Player chooses Rock
    if ((player == 'Rock') and (computer == 'Rock')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Rock') and (computer == 'Paper')):
        print('Computer Wins as Paper covers Rock!')
        winner = 'computer'
        return winner
    elif ((player == 'Rock') and (computer == 'Scissors')):
        print('Player Wins as Rock breaks Scissors!')
        winner = 'player'
        return winner
    elif ((player == 'Rock') and (computer == 'Lizard')):
        print('Player Wins as Rock crushes Lizard!')
        winner = 'player'
        return winner
    elif ((player == 'Rock') and (computer == 'Spock')):
        print('Computer Wins as Spock vaporizes Rock!')
        winner = 'computer'
        return winner
    
    # Player chooses Paper
    if ((player == 'Paper') and (computer == 'Paper')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Paper') and (computer == 'Rock')):
        print('Player Wins as Paper covers Rock!')
        winner = 'player'
        return winner
    elif ((player == 'Paper') and (computer == 'Scissors')):
        print('Computer Wins as Scissors cuts Paper!')
        winner = 'computer'
        return winner
    elif ((player == 'Paper') and (computer == 'Lizard')):
        print('Computer Wins as Lizard eats Paper!')
        winner = 'computer'
        return winner
    elif ((player == 'Paper') and (computer == 'Spock')):
        print('Player Wins as Paper disproves Spock!')
        winner = 'player'
        return winner
  
    # Player chooses Scissors
    if ((player == 'Scissors') and (computer == 'Scissors')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Scissors') and (computer == 'Paper')):
        print('Player Wins as Scissors cuts Paper!')
        winner = 'player'
        return winner
    elif ((player == 'Scissors') and (computer == 'Rock')):
        print('Computer Wins as Rock breaks Scissors!')
        winner = 'computer'
        return winner
    elif ((player == 'Scissors') and (computer == 'Lizard')):
        print('Player Wins as Scissors decapitate Lizard!')
        winner = 'player'
        return winner
    elif ((player == 'Scissors') and (computer == 'Spock')):
        print('Computer Wins as Spock melts Scissors!')
        winner = 'computer'
        return winner
    
    # Player chooses Lizard
    if ((player == 'Lizard') and (computer == 'Lizard')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Lizard') and (computer == 'Paper')):
        print('Player Wins as Lizard eats Paper!')
        winner = 'player'
        return winner
    elif ((player == 'Lizard') and (computer == 'Rock')):
        print('Computer Wins as Rock cruches Lizard!')
        winner = 'computer'
        return winner
    elif ((player == 'Lizard') and (computer == 'Scissors')):
        print('Computer Wins as Scissors decapitate Lizard!')
        winner = 'computer'
        return winner
    elif ((player == 'Lizard') and (computer == 'Spock')):
        print('Player Wins as Lizard poisons Spock!')
        winner = 'player'
        return winner
    
    # Player chooses Spock
    if ((player == 'Spock') and (computer == 'Spock')):
        print('Tie')
        winner = 'tie'
        return winner
    elif ((player == 'Spock') and (computer == 'Paper')):
        print('Computer Wins as Paper disproves Spock!')
        winner = 'computer'
        return winner
    elif ((player == 'Spock') and (computer == 'Rock')):
        print('Player Wins as Spock vaporizes Rock!')
        winner = 'player'
        return winner
    elif ((player == 'Spock') and (computer == 'Scissors')):
        print('Player Wins as Spock melts Scissors!')
        winner = 'player'
        return winner
    elif ((player == 'Spock') and (computer == 'Lizard')):
        print('Computer Wins as Lizard poisons Spock!')
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
    print('Player Score   -', playerScore, 'winning % -',(f"{((playerScore / (playerScore + computerScore + ties)) * 100):.2f}%"))
    print('Computer Score -', computerScore, 'winning % -',  (f"{((computerScore / (playerScore + computerScore + ties)) * 100):.2f}%"))
    print('Ties           -', ties, 'tie %     -',   (f"{((ties / (playerScore + computerScore + ties)) * 100):.2f}%"))
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