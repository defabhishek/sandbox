n,k = map(int,input().strip().split())
lst = [int(i) for i in input().strip().split()]
count = 0
for i in lst:
    if (i >= lst[k-1]) and (i>0):
        count += 1
print(count)