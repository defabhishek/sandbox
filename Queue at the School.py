n,t = map(int,input().strip().split())
lst = [i for i in input().strip()]
for j in range(t):
    i = 0
    while i < len(lst)-1:
            if (lst[i] == 'B') and (lst[i+1] == 'G'):
                lst[i],lst[i+1] = lst[i+1],lst[i]
                i += 1
            i += 1
print("".join(lst))