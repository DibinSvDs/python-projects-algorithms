import random
random_number = random.randint(1, 100)
user_points = 0
game_over = False

while game_over == False:
    user_number = int(input("Enter a Number: "))

    if user_number > random_number:
        print("Please Enter a Lower Number")
        user_points -= 10

    elif user_number < random_number:
        print("Please Enter a Higher Number")
        user_points -= 10

    else:
        print("You Win!")
        game_over = True
        user_points += 300
