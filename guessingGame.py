import random

def myGuess():
    print("Please choose a number from 0 to 100")
    guess = random.randint(2,98)
    upperLower = input("Is " + str(guess) + " (h)igh, (l)ow, or (c)orrect? ")
    guessAdjust(guess, upperLower)

def guessAdjust(guess, adjustment):
    if(adjustment == 'c'):
        print("Awesome!")
    elif(adjustment == 'l'):
        guess = random.randint(int(guess)+1, 100)
        upperLower = input("Is " + str(guess) + " (h)igh, (l)ow, or (c)orrect? ")
        guessAdjust(guess, upperLower)
    elif(adjustment == 'h'):
        guess = random.randint(0,int(guess)-1)
        upperLower = input("Is " + str(guess) + " (h)igh, (l)ow, or (c)orrect? ")
        guessAdjust(guess, upperLower)

def theirGuess():
    n = random.randint(0,100)
    print("My number is between 0 and 100.")
    guess = int(input("What's your guess? "))
    while(guess != n):
        if(guess > n):
            guess = int(input("Too high! Guess again: "))
        elif(guess < n):
            guess = int(input("Too low! Guess again: "))
    print("Correct! Good job!")
    
print("Would you like to guess my number (1) or have me guess yours (2)?")
chose = ""
while(chose != "1" and chose != "2"):
    chose = input("1 for your guess, 2 for mine: ")
    if(chose == "1"):
                theirGuess()
    elif(chose == "2"):
                myGuess()
