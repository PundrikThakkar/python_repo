import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalue, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

turn = 0

print("\nPlayer", turn + 1, "turn has just started!\n")

while max(player_scores) < max_score:

    curr_score = player_scores[turn]
    should_roll = input("Would you like to roll (y)? ").lower()
    if should_roll != "y":
        if turn < (players - 1):
            turn += 1
        else:
            turn = 0

        print("\nPlayer", turn + 1, "turn has just started!\n")

        continue

    value = roll()
    if value == 1:
        print("\nYou rolled a 1! Turn done!")
        if turn < (players - 1):
            turn += 1
        else:
            turn = 0

        print("\nPlayer", turn + 1, "turn has just started!\n")

    else:
        print(f"Player {turn+1} rolled:", value)
        curr_score += value
        player_scores[turn] = curr_score
        print(f"Player {turn+1} score is:", player_scores[turn])

winning_score = max(player_scores)
winning_player = player_scores.index(winning_score) + 1

print(f"\n---Player {winning_player} won with score : {winning_score}---\n")
