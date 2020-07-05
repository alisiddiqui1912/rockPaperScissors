import random

player = input("Make your move: ").lower()

rand_num = random.randint(0,2)


if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
	computer = "scissors"

print("Computer move is: " + computer)

if player == computer:
	print("It's a tie.")
elif player == "rock":
	if computer == "scissors":
		print("You win!!")
	else:
		print("computer wins!!")	
elif player == "paper":
	if computer == "rock":
		print("You win!!")
	else:
		print("computer wins!!")
elif player == "scissors":
	if computer == "rock":
		print("computer wins!!")
	else:
		print("You win!!") 
else:
	print("Plese enter valid move.")