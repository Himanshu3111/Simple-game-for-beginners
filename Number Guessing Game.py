import random

secret = random.randint(1, 10)
tries = 0

print("I am thinking of a number from 1 to 10.")

while True:
    guess = int(input("Your guess: "))
    tries = tries + 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("You got it in", tries, "tries!")
        break
