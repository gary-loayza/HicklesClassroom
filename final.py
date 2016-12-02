##################################
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
    print('Take a guess.')
    myGuess = int( input())

		# Counts my guesses
    guessesTaken = guessesTaken + 1

    if myGuess < number:
        print('Your guess is too low.')

    if myGuess > number:
        print('Your guess is too high.')


    # Computer tells me when I get the right answer.
    if myGuess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
        break


# Computer tells me what the number was if I lose.
if myGuess != number:
    number = str(number)
    print('Sorry. The number I was thinking of was ' + number)


