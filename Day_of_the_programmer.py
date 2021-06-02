
def dayOfProgrammer(year):
    if year >= 1918:
        print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            return f'12.09.{year}'
        elif year == 1918:
            return '26.09.1918'
        else:
            return f'13.09.{year}'
    elif year < 1918:
        # never use bools in list like [True] in conditionals
        if (year % 4 == 0):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'


year = 1711
print(dayOfProgrammer(year))
