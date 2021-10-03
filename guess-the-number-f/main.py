import random

class GuessTheNumber:
    def __init__(self, number, min=1, max=100):
        self.number = number
        self.guess = 1
        self.min = min
        self.max = max
        self.userInput()

    def userInput(self):
        try:
            n = int(input("Enter a Number Between {} and {}: ".format(self.min, self.max)))
            return self.play(n)
        except:
            print("Enter a Valid Number")
            self.userInput()

    def play(self, n):
        self.n = n
        if n > self.number:
            print("Enter a Smaller Number")
            self.guess += 1
            self.userInput()
        elif n == self.number:
            print("You Win!, You Finished This Game in {} guesses".format(self.guess))
        else:
            print("Enter a Larger Number")
            self.guess += 1
            self.userInput()
rn = random.randint(1, 100)
g = GuessTheNumber(rn, 1, 100)
g