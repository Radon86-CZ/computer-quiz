print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ").lower()
if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does USB stand for? ").lower()
if answer == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for? ").lower()
if answer == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does LAN stand for? ").lower()
if answer == "local area network":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does IP stand for? ").lower()
if answer == "internet protocol":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score / 10) * 100) + "%.")