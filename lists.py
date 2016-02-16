one, two, three, four = ["France", "Feb 15th", "Burgers", "Money"]

print two


def middle(grades):
    yesboy = []
    # first, *middle, end = grades
    end = grades[-1]
    start = grades[0]
    # print end
    # print start
    for i in grades:
        if i != start and i != end:
            yesboy.append(i)
            if len(yesboy) > 2:
                print yesboy


middle([60, 54, 23, 65, 76])
