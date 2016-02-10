my_list = raw_input("Enter a sentence: ")

other = ["a", "e", "w", "x"]

vowels = list('aeiou')


new_sentence = []

if my_list == "reversed":
    newer = raw_input(">")
    for i in newer:
        if i not in vowels:
            new_sentence.append(i)
    print ''.join(new_sentence[::-1])
else:
    for i in my_list:
        if i not in vowels:
            new_sentence.append(i)
    print ''.join(new_sentence)
