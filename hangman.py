import random


def game():
    while True:

        num = int(input("Pick a number and let the computer guess: "))
        comp_guess = random.randint(1, 10)
        print "computer guessed: %s" % comp_guess
        if comp_guess == num:
            print("Computer wins")
            break
        else:
            print "That's not it"


game()