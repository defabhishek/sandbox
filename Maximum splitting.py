# 90 = 4+4+...+6
def maxSummation(dp_array,n,start=4):
    if n==0:
        return 0
    if n<4:
        return -1
    for i in range(start,n):
        if not dp_array[i]:
            continue
        if not n%i:
            return n/i
        for j in range(n//i,0,-1):

n = int(input())
while n:
    n-=1
    a = int(input())
    dp_array = [False]*(a+1)
    for i in range(2,a+1):
        if dp_array[i]:
            continue
        for j in range(2*i,a+1,i):
            dp_array[j] = True
    if a<4:
        print(-1)
    print(dp_array)