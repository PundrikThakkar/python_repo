import random

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit.").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    computer_pick = options[random.randint(0, 2)].lower()

    if user_input == "rock":
        if computer_pick == "rock":
            print("Tie!")
        elif computer_pick == "paper":
            computer_score += 1
            print("Computer Win!")
        else:
            user_score += 1
            print("User win!")
    elif user_input == "paper":
        if computer_pick == "rock":
            user_score += 1
            print("User Win!")
        elif computer_pick == "paper":
            print("Tie!")
        else:
            computer_score += 1
            print("Computer Win!")
    else:
        if computer_pick == "rock":
            computer_score += 1
            print("Computer Win!")
        elif computer_pick == "paper":
            user_score += 1
            print("User Win!")
        else:
            print("Tie!")

        print("Computer had pick", computer_pick)

print("User won", user_score, "times.")
print("Computer won", computer_score, "times.")

print("Goodbye!")
