def sockMerchant(n, ar):
    # Write your code here
    dict_count = {i:ar.count(i) for i in ar}
    pairs = 0
    for v in dict_count.values():
        pairs+=v//2 #to get the quotient, % is used for remainder
    #print(pairs, dict_count)
    return pairs

a = 9
ar= [10, 20, 20, 10, 10, 30, 50, 10, 20]

print(sockMerchant(a,ar))
