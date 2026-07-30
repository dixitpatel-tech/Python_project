import random

while True: #loop start

    choices = ["snake", "water", "gun"]

    # User input
    you = input("Enter snake, water or gun: ")

    # computer random choice
    computer = random.choice(choices)

    if you == "exit":
        print("Game And")
        break  #loop stop

    # Show choices
    print("You chose:", you)
    print("Computer chose:", computer)

    # Game logic
    if (computer == you):
        print("It's a draw")

    else:
        if (computer == "water" and you == "snake"):
            print("You win!")
        
        elif (computer == "water" and you == "gun"):
            print("You lose!")
        
        elif (computer == "snake" and you == "water"):
            print("You lose!")
        
        elif (computer == "snake" and you == "gun"):
            print("You win!")
        
        elif (computer == "gun" and you == "water"):
            print("You win!")
        
        elif (computer == "gun" and you == "snake"):
            print("You lose!")
        
        else:
            print("Invalid input")