#################################
##################################
#
# This is a guess the number game.
#
##################################
##################################


# Computer thinks of a random number between 1 and 20
import random
number = random.randint(1, 20)


# Computer asks me for my name and remembers myName
print('Hello! What is your name?')
myName = input()


# Computer asks me to make a guess and remembers myGuess
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')


# Computer gives me 6 tries
guessesTaken = 0

while guessesTaken < 6:
    print('Take a guess!')
    myGuess = int( input())


    # Computer remembers how many guessesTaken and adds one
    guessesTaken = guessesTaken + 1


    # Computer tells me if myGuess is right
    if myGuess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
        break


    # Computer tells me if myGuess is wrong
    if myGuess != number:
        print('Wrong!')


