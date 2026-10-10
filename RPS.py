import random

choices = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!")

while True:
    player = input("Type rock, paper, or scissors (or quit): ").lower()

    if player == "quit":
        print("Thanks for playing. Bye!")
        break

    if player not in choices:
        print("Wrong word. Please try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")
