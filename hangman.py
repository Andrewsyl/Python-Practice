import random

my_list = ['apples', 'pineapple', 'oranges', 'bananas', 'grapefruit', 'lemon', 'strawberry']

good_guesses = []
bad_guesses = []

secret_word = random.choice(my_list)

while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
    for guess in secret_word:
        if guess in good_guesses:
            print guess,'',
        else:
            print '_',

    guess = raw_input("Guess a letter: ").lower()

    if guess in secret_word:
        print "That's in"
        good_guesses.append(guess)
        if len(good_guesses) == len(secret_word):
            print("You freakin' win!")
            break

        print "\n**You have %s more chances**\n" % -(len(bad_guesses) - 7)
    elif len(guess) != 1:
        print "Only one at a time"
        continue
    elif guess in good_guesses or guess in bad_guesses:
        print "You have already guessed that letter"
        continue
    elif not guess.isalpha():
        print "That's not a letter"
        continue
    elif guess not in secret_word:
        print "Nope, that's not in the secret word"
        bad_guesses.append(good_guesses)

    else:
        print "You didn't win, my secret work was %s" % secret_word.upper()
