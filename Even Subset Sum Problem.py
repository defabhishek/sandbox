T = int(input())
while T>0:
    T-=1
    n = int(input())
    lst = [int(x) for x in input().strip().split()]
    if len(lst) == 0:
        print(-1)
        continue
    if len(lst) == 1 and lst[0]%2:
        print(-1)
        continue
    d = lst[0]
    if not d%2:
        print("1\n1")
        continue
    if lst[1]%2:
        print("2\n1 2")
    else:
        print("1\n2")