import random

picked_number = int(input("Pick a number between one and ten: "))
computer_guess = int(random.randint(1, 10))

#print computer_guess

bad_guesses = []

if picked_number == computer_guess:
    print "comp got the number"
else:
    print computer_guess
    while True:
        hint = raw_input("Is your guess higher or lower? ").lower()
        if hint == "h":
            new_comp_guess = random.randint(computer_guess, 10)
            print new_comp_guess
            if new_comp_guess == computer_guess:
                continue
            elif new_comp_guess == picked_number:
                print "comp wins!"
                break
            elif new_comp_guess in bad_guesses:
                print "same"
                continue
            else:
                bad_guesses.append(new_comp_guess)

        elif hint == "l":
            new_comp_guess = random.randint(0, computer_guess)

            print new_comp_guess
            if new_comp_guess == picked_number:
                print "comp wins"
                break
            elif new_comp_guess == computer_guess:
                continue
            elif new_comp_guess in bad_guesses:
                pass
            else:
                bad_guesses.append(new_comp_guess)

if len(bad_guesses) != 0:
    print bad_guesses