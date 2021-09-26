import random
rand = random.randint(1, 3)
comp = ""
if rand == 1:
    comp = "R"
elif rand == 2:
    comp = "P"
else:
    comp = "S"

print("Welcome! to Rock Paper Scissors Game")
u = input()
if u == "R":
    if comp == "P":
        print("Computer Won")
    elif comp == "S":
        print("You Won")
    else:
        print("Match Tied!")
