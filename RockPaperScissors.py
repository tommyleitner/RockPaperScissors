import random

user_wins = 0
computer_wins = 0
draw = 0 

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break                                                               #Bricht die While True Schleife und dann sind wir am Ende
    
    if user_input not in options:
        print("Wrong input, try again!")
        continue                                                            #Springt wieder zum Anfang von While True

    random_number = random.randint(0,2)
    # Rock -> 0, Paper -> 1, Scissors -> 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It is a draw!")
        draw += 1

    else:
        print("You lost!")
        computer_wins += 1


print("---------------------------------------")
print("You won", user_wins, "times.")
print("The Computer won", computer_wins, "times.")
print("Draw", draw, "times.")
print("---------------------------------------")
print("Thank you for playing!")
print("Goodbye!")