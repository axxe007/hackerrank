def birthday(s, d, m):
    ways = 0

    for j, i in enumerate(s):
        try:
            if sum(s[j:j+m]) == d:
                ways += 1
        except:
            pass
    return print(ways)


s = [1, 2, 1, 2, 2]
d = 3
m = 2

birthday(s, d, m)
