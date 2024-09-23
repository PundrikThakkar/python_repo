print("Welcome to Computer Quiz.")

consent = input("Do you wanna play a game? ")

if consent.lower() != "yes":
    quit()

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    score += 1
    print("Correct!")
else:
    print("Incorrect!")


print("Your final score is", score, ".")
print("Your percentage wise result =", (score / 3) * 100, "%.")
