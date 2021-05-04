q,t = map(int,input().strip().split())
# s = (5*n/2)(1 + n) = (5*(n**2)/2 + 5*n/2 < 240-t
for n in range(q,-1,-1):
    if (5*n + 5*(n**2))/2 <= (240-t):
        print(n)
        break