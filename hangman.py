import random

my_list = ['paris', 'london', 'dublin', 'newyork', 'losangelas', 'colorado', 'mississippi']

good_guesses = []
bad_guesses = []

secret_word = random.choice(my_list)

print secret_word

while len(bad_guesses) < 7