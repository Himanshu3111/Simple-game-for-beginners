print("Welcome to the Treasure Hunt!")
print("You are standing in a forest. You must find the treasure.")
print()

path = input("You see two paths. Go left or right? ").lower()

if path == "left":
    print("You walk and find a river.")
    action = input("Swim across or build a boat? ").lower()

    if action == "boat":
        print("Good idea! You cross the river safely.")
        print("You see a cave.")
        door = input("Enter the cave or go around? ").lower()

        if door == "enter":
            print("You find a big box full of gold!")
            print("YOU WIN! You found the treasure!")
        else:
            print("You walk for many hours and get lost.")
            print("GAME OVER.")
    else:
        print("The water is too strong. You are taken away.")
        print("GAME OVER.")

elif path == "right":
    print("You walk and meet a tiger!")
    action = input("Run or stay still? ").lower()

    if action == "stay":
        print("The tiger looks at you and goes away.")
        print("You find a small house.")
        door = input("Knock on the door or go inside? ").lower()

        if door == "knock":
            print("An old man opens the door and gives you a map.")
            print("The map leads you to the treasure.")
            print("YOU WIN! You found the treasure!")
        else:
            print("The old man is angry and sends you away.")
            print("GAME OVER.")
    else:
        print("The tiger is faster than you.")
        print("GAME OVER.")

else:
    print("You did not choose a path. You wait and the night comes.")
    print("GAME OVER.")
