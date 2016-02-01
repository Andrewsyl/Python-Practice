import random
import os
import sys

my_list = ['apples', 'pineapple', 'oranges', 'bananas', 'grapefruit', 'lemon', 'strawberry']

# file = open('C:/Users/Andrew/PycharmProjects/treehousetests/secret_words.txt', 'r')
# print file.read(1)
# file.close()


def play_again():
    print "Play Hangman?"

    again = raw_input("Yes/No: ").upper()
    if again == "YES":
        print "\nGreat,let's play!\n"
        play(done)
    elif again == "NO":
        print "\n**Thanks for playing, Goodbye**"
        sys.exit()
    else:
        print "Sorry what?"
        play_again()


def clear():
    os.system('cls')
    # os.system('clear')


def draw(bad_guesses, good_guesses, secret_word, lives_left):
    clear()
    # lives_left = lives(secret_word)
    print ''
    print "**You have %s chances left**" % lives_left
    # print "**You have %s chances left**" % -(len(bad_guesses) - 7)
    print "SECRET WORD: "
    for guess in secret_word:
        if guess in good_guesses:
            print guess, '',
        else:
            print '_',
    print ''
    print 'Bad Guesses: '
    for guess in bad_guesses:
        if guess in bad_guesses:
            print guess, '',

    print('\n')


def get_guess(good_guesses, bad_guesses):
    while True:
        guess = raw_input("Guess a letter: ").lower()

        if guess in good_guesses or guess in bad_guesses:
            print "You have already guessed that letter"

        elif len(guess) > 1:
            print "Only one at a time"

        elif not guess.isalpha():
            print "That's not a letter"
        else:
            return guess


def lives(secret_word):
    if len(secret_word) >= 7:
        lives_length = 8
        return lives_length
    else:
        lives_length = 5
        return lives_length


def play(done):
    good_guesses = []
    bad_guesses = []
    secret_word = random.choice(my_list)
    lives_left = lives(secret_word)

    while lives_left > 0:
        draw(bad_guesses, good_guesses, secret_word, lives_left)
        guess = get_guess(good_guesses, bad_guesses)

        if guess in secret_word:
            print "Well done! **%s** is in the secret word" % guess
            good_guesses.append(guess)
            found = True
            for guess in secret_word:
                if guess not in good_guesses:
                    found = False
            if found:
                print "You win"
                print "The secret word was %s" % secret_word.upper()
                done = True
        else:
            print "Nope, that's not in the secret word"
            bad_guesses.append(guess)
            lives_left -= 1
            if lives_left == 0:
                draw(bad_guesses, good_guesses, secret_word, lives_left)
                print "You didn't get it"
                print "The secret word was %s" % secret_word.upper()
                done = True

        if done:
            play_it = raw_input("play again? y/n ").lower()
            if play_it != 'n':
                print "\n**Good stuff, let's play again**"
                return play(done=False)

            else:
                print "\n***Thanks for playing***"
                sys.exit()


done = False

while True:
    play_again()
    play(done)
