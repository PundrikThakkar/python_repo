import random

print("---WELCOME TO NUMBER GUESSING GAME---")

top_of_range = input("Type a number: ")

if top_of_range.isdigit() != True:
    print("Please type a number next time.")
    quit()

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()

final_number = random.randint(1, top_of_range)

print("---> GUESS THE NUMBER FROM 1 TO ", top_of_range, "<---")


count = 0

while True:
    guessing_number = input("TYPE YOUR NUMBER: ")
    if guessing_number.isdigit() != True:
        print("Please type number next time.")
        quit()

    guessing_number = int(guessing_number)
    if guessing_number == final_number:
        count += 1
        print("YOU WIN! IN ", count, "ATTEMPTS.")
        break
    elif guessing_number < final_number:
        count += 1
        print("YOUR GUESS IS TOO LOW! GUESS AGAIN.")
        continue
    else:
        count += 1
        print("YOUR NUMBER IS TOO HIGH! GUESS AGAIN.")
        continue
