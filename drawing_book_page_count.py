def pageCount(n, p):
    # Write your code here
    count_front = 0
    count_back = 0
    if p>(n//2):
        if n%2 == 0:
            count_back = (n-p+1)//2
        else:
            count_back = (n-p)//2
        return count_back
    else:
       count_front = (p)//2
       return count_front

n = 5
p = 4
print(pageCount(n,p))
