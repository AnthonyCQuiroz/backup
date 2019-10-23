# Anthony Quiroz
# Rock Paper Scissors
# rps.py
# added comment for github
import random 
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

# Welcome Message
# Print welcome message
print("Welcome to Rock Paper Scissors")
# prompt for name
pName = input("What is your name? ")


# Score tracker
# Make a function
def printScore():
	# Prints score:
	print("Score: ")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score 
	print("Computer score: " + str(cScore))
# Shows how many ties
	print("Ties: " + str(ties))

# Game loop
# Loop until q is entered 
while True:
	# prompt for player move (r, p, s, q)
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to Quit" )
# print the score
	printScore()
# Check if q is entered if so end the game
	if pMove == 'q':
		break
# get a computer move (random)
	cMove = random.choice(cMoves)
# compare the player move with the computer move
	# Player picks rock 
	if pMove == "r":
		print(pName + " picked Rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Tie")
			ties += 1 
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else:
			print("Computer picks Scissors")
			print("Rock breaks scissors")
			pScore += 1
# Player picks paper
	elif pMove == "p":
		print(pName + " picked Paper")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Paper covers rock")
			cScore += 1 
		elif cMove == "paper":
			print("Computer picks Paper")
			print("This is a tie")
			ties += 1
		else:
			print("Computer picks Scissors")
			print("Scissors cuts paper")
			pScore += 1
# Player picks scissors
	elif pMove == "s":
				print(pName + " picked Rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Rock breaks Scissors")
			cScore += 1 
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Scissors cuts paper")
			pScore += 1
		else:
			print("Computer picks Scissors")
			print("This is a tie")
			ties += 1
# check if pMove is valid
	else:
		print("That is not an option")