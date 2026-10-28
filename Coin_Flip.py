import random

score = 0

print("Welcome to the Coin Flip Game!")

while True:
    guess = input("Heads or tails? (or type quit): ").lower()

    if guess == "quit":
        break

    if guess != "heads" and guess != "tails":
        print("Please type heads or tails.")
        continue

    coin = random.choice(["heads", "tails"])
    print("The coin shows:", coin)

    if guess == coin:
        print("You win!")
        score = score + 1
    else:
        print("You lose!")

    print("Your wins:", score)
    print()

print("Thanks for playing! Your final wins:", score)
