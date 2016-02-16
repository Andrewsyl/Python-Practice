import sys

shopping_list = []


def showlist():
    count = 1
    for item in shopping_list:
        print ("{} : {}").format(count, item)
        count += 1

def thing():
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
            # elif not item.isalpha():
            #     print "That's not an item, please try again"
            #     continue
            elif item == 'remove':
                showlist()
                print ''
                item_remove = raw_input("What would you like to remove?: ").lower()

                if item_remove not in shopping_list:
                    print "That's not on your list"
                    continue
                for i in shopping_list:
                    if i == item_remove:
                        shopping_list.remove(i)
                        print "{} removed".format(i)


def add():
    print "\nWelcome to the store, add items to your list!\n"
    print "\nType: 'Done' at anytime to finish."
    print "Type: 'Remove' to remove any unwanted items.\n"

    item = thing()

    while True:
        new_list = item.split(',')
        try:
            index = input("Where on the list would you like {} to be placed at?: ".format(item))
            if index > len(new_list):
                print "{} added to end of the list".format(item)
            else:
                print "{} added".format(item)
            pass
        except NameError:
            print "That's not a number, please enter a number"
            continue
        except TypeError:
            print "That's not a number, please enter a number"
            continue

        for i in new_list:
            shopping_list.insert(int(index) - 1, i)
        break

    print "Thanks for shopping"
    print "Goodbye"


add()