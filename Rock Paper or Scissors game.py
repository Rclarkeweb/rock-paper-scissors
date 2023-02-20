# Rock Paper Scissors Terminal/Console game

# User types name and chooses rock, paper or scissors
user = input('Whats your name? ')
print("Hello ", user)
player = input('Type your choice of Rock, Paper or Scissors: ')

# Correct for capitals and if user mistyped
if player == "Rock" or player == 'rock':
    player = 'Rock'
    print(user, "chose: ", player)
elif player == "Scissors" or player == 'scissors':
    player = 'Scissors'
    print(user, "chose: ", player)
elif player == "Paper" or player == 'paper':
    player = 'Paper'
    print(user, "chose: ", player)
else:
    print('Oops, type a different choice, start again')

# import random module
import random 

# Create random integar between 1 and 3
computer = random.randint(1, 3)

# Assign the computers chosen number a rock, paper or scissors option
if computer == 1:
    computerscore = 'Rock'
    print("Computer chose", computerscore)
elif computer == 2:
    computerscore = 'Paper'
    print("Computer chose", computerscore)
else:
    computerscore = 'Scissors'
    print("Computer chose", computerscore) 

# Print the choices
print(player, 'vs', computerscore)

# Print who wins
if computerscore == player:
    print("Its a draw!")
elif player == 'Rock' and computerscore == 'Paper':
    print('Computer wins')
elif player == 'Paper' and computerscore == 'Scissors':
    print("Computer wins")
elif player == 'Scissors' and computerscore == 'Rock':
    print('Computer wins')
elif player == 'Rock' and computerscore == 'Scissors':
    print(user, 'wins!')
elif player == 'Paper' and computerscore == 'Rock':
    print(user, 'wins!')
elif player == 'Scissors' and computerscore == 'Paper':
    print(user, 'wins!')

# End of game
print("Game over!")
