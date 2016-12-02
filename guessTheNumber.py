####################################
####################################
#
# This is the guess the number game.
#
####################################
####################################


# Computer thinks of a random number between 1 and 20
import random
number = random.randint(1, 20)


# Computer asks me for my name and remembers myName
print('Hello! What is your name?')
myName = input()


# Computer asks me to make a guess and remembers myGuess
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
print('Take a guess!')
myGuess = int( input())


# Computer tells me if myGuess is right
if myGuess == number:
    print('Good job, ' + myName + ' You got it!')


# Computer tells me if myGuess is wrong
if myGuess != number:
    print('Wrong!')


