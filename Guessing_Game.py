import random

def start():
    global numberToGuess, guesses
    guesses = 10
    numberToGuess = random.randint(1,20)
    print("A random number has been generated!")
def highLow(a,b):
    if a > b:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
def gameEndCheck():
    if guesses == 0:
        print("You Lost! The number was {}!" .format(numberToGuess))
    else:
        print("You Won! It took you {} guesses to pick the number {}!" .format(11-guesses,numberToGuess))

#========== GAME STARTS HERE ==========
input('''
Welcome to the Guessing Game!
   /press enter to begin/
''')

start()
while guesses != 0:
    try:
        inputNum = int(input("Pick a number between 1 and 20 [{} guesses left!]: " .format(guesses)))
        if inputNum == numberToGuess:
            break;
        else:
            highLow(inputNum,numberToGuess)
            guesses-=1
    except ValueError:
        print("Please enter an integer [:P]")
gameEndCheck()


"""
========== LOGS ==========
Sir I used functions like start(), highLow(), and gameEndCheck()
because it would be eaisier to read the code that way rather than
compressing all the code into a single while loop xD
==========================

"""
