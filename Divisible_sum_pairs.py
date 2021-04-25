def divisibleSumPairs(n, k, ar):
    divisible = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                divisible += 1

    return print(divisible)


n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
divisibleSumPairs(n, k, ar)
