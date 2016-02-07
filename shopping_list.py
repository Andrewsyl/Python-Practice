import sys

shopping_list = []


def showlist():
    count = 1
    for item in shopping_list:
        print ("{} : {}").format(count, item)
        count += 1


def remove(num):
    shopping_list.remove(num)


def add():
    print "Welcome to the store, add items to your list!\n"
    while True:
        item = raw_input("What would you like to add?: ").lower()
        if item == "show":
            print "\nHere's your list"
            showlist()
            continue
        elif item == "done":
            print "Here's your list"
            showlist()
            break

        elif item == 'remove':
            new = raw_input("What would you like to remove?: ")
            if new not in shopping_list:
                print "That's not on your list"
                continue
            for i in shopping_list:
                if i == new:
                    shopping_list.remove(i)
                    print "{} removed".format(i)
        else:
            new_list = item.split(',')
            try:
                index = input("Give me a number to out the item at: ")
                print "{} added".format(item)
                pass
            except NameError:
                print "That's not a number, please enter item(s) again"
                continue

            for i in new_list:
                shopping_list.insert(int(index) - 1, i)

    print "Thanks for shopping"


add()

# import os,glob
#
# os.chdir('/Users/andrew/desktop/image dump')
# for i in glob.glob('*.jpg'):
#     print(i)
