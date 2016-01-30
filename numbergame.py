import random


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


def guessing_game():
    num = random.randint(1, 10)
    lives = 6
    while True:

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
        elif guess > num:
            print "\n**Too High**"
            lives -= 1
            print "Lives left: %s\n " % lives
        elif guess < num:
            print "\n**Too Low**"
            lives -= 1
            print "Lives left: %s\n " % lives
        elif lives < 2:
            print "GAME OVER"
            break

    play_again()

want_to_play()
