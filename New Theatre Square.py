T = int(input())
while T>0:
    T-=1
    cost,count = 0,0
    n,m,x,y = map(int,input().strip().split())
    arr = []
    for i in range(n):
        arr.append([])
        arr[i] = [x for x in input()]
    i,j =0,0
    while i<n:
        j=0
        while j<m:
            if arr[i][j] == '.':
                count+=1
            if arr[i][j] == '*':
                j+=1
                continue
            if j<(m-1):
                if arr[i][j+1] == '.':
                    count+=1
                    cost+=y
                    j+=2
                    continue
            cost+=x
            j+=1
        i+=1
    print(min(cost,count*x))




