def bonAppetit(bill, k, b):
    shares_brian = (sum(bill)+bill[k])/2
    shares_anna = (sum(bill) - bill[k])/2
    if shares_anna == b:
        return print('Bon Appetit')
    else:
        return print(int(bill[k]/2))


bill = [3, 10, 2, 9]
n = 4
k = 1
b = 12

bonAppetit(bill, k, b)
