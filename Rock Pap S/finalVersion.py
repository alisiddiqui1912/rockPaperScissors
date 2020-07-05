import random

player_win = 0
computer_win = 0
win_score = input("Enter the Winning Score: ")
win_score = int(win_score)

while win_score > player_win and win_score > computer_win: 
	print(f"Your Score:{player_win},Computer Score:{computer_win}")
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
			player_win += 1
		else:
			print("computer wins!!")
			computer_win += 1	
	elif player == "paper":
		if computer == "rock":
			print("You win!!")
			player_win += 1
		else:
			print("computer wins!!")
			computer_win += 1
	elif player == "scissors":
		if computer == "rock":
			print("computer wins!!")
			computer_win += 1
		else:
			print("You win!!") 
			player_win += 1
	else:
		print("Plese enter valid move.")

print(f"Final Score:-Your Score:{player_win},Computer Score:{computer_win}")
if player_win > computer_win:
    print("You Win!!")
else:
 	print("Computer Wins")