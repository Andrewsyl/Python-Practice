import random
import os


def want_to_play():
    start = raw_input("Do you want to play? Yes or No? ").upper()
    if start == "YES":
        print "\n***Ok great, let's play!***\n"
        guessing_game()
    elif start == "NO":
        print "Ok, maybe next time"
    else:
        print "Sorry, what?"
        want_to_play()


def play_again():
    print "Play again?"

    again = raw_input("Yes/No: ").upper()
    if again == "YES":
        print "\nGreat,let's play!\n"
        guessing_game()
    elif again == "NO":
        print "\n**Thanks for playing, Goodbye**"
    else:
        print "Sorry what?"
        play_again()


def clear():
    os.system('cls')
    # os.system('clear')


def difficulty():
    while True:
        lives = raw_input("What difficulty, \nEasy\nMedium\nHard?: ").upper()
        if lives == "HARD":
            hearts = 3
            print "You selected {}. That gives you {} lives".format(lives, hearts)
            return hearts
        elif lives == "MEDIUM":
            hearts = 5
            print "You selected {}. That gives you {} lives".format(lives, hearts)
            return hearts
        elif lives == "EASY":
            hearts = 7
            print "You selected {}. That gives you {} lives".format(lives, hearts)
            return hearts
        else:
            print "That's not a difficulty, try again"

def guessing_game():
    num = random.randint(1, 10)
    lives = difficulty()
    bad_gueses = []
    clear()
    while lives > 0:

        try:
            guess = int(input("Guess a number between 1-10: "))
            pass
        except NameError:
            print "That's not a number, try again"
            continue
        except SyntaxError:
            continue

        if guess == num:
            print "You got it, well done!"
            break
        elif guess in bad_gueses:
            print "You already guessed that, try again"
            continue
        elif guess > num:
            print "\n**Too High**"
            lives -= 1
            bad_gueses.append(guess)
            print "Lives left: %s\n " % lives
            print "Bad guesses: %s" % bad_gueses
        elif guess < num:
            print "\n**Too Low**"
            lives -= 1
            print "Lives left: %s\n " % lives
            bad_gueses.append(guess)
            print "Bad guesses: %s" % bad_gueses

    else:
        print "GAME OVER"
        print "The secret number was %s" % num

    play_again()


want_to_play()
