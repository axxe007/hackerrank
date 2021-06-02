steps = input("number of steps")
# path = ""
path = input("steps taken")
# print(countingValleys(steps, path))
# because the question is unable to explain the problem Let me add one more example

# __/\        __  = UDDUDUDUDU with 10 steps, answer should be 4.
#     \/\/\/\/


def countingValleys(steps, path):
    dist = {"U": 1, "D": -1}
    valley, total = 0, 0
    for i in path:
        # first condition mean: previous location + present step = sea level
        # second condition mean: previous position should be below sea level
        # and if both conditions are met, that means we are coming from below sea level(-ve to 0) to
        # sea level, so our valley ends here.
        if (total+dist[i] == 0) and total < 0:
            valley += 1
        total += dist[i]
    return valley


print(countingValleys(steps, path))
