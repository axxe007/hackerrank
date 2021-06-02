from typing import Counter
import operator


arr = [1, 1, 1, 1, 2, 3, 4, 2, 2, 4, 5, 5, 3, 1, 2, 3, 4, 5, 2, 2, 5, 5, 5]


def migratoryBirds(arr):
    sights = Counter(arr)

    # print(sights)

    max_value = max(sights.values())

    # max(sights.items(), key=operator.itemgetter(1)) # Since dict are not ordered,
    # we will be getting first key with largest value even if it is not the one we need.
    # So we need to get keys of sights which have that max value.
    maximum_pairs = []

    # print(max_value)

    for key in sights.keys():
        if max_value == sights[key]:
            maximum_pairs.append(int(key))

    return min(maximum_pairs)


with open('Migratory_bird_test_case.txt', 'r') as line:
    data = line.readline().split(' ')

data = [int(x) for x in data]

print(migratoryBirds(data))
