# 2 1 2 2 1 2 2
T = int(input())
while T>0:
    T -= 1
    n = int(input())
    lst = [int(x) for x in input().strip().split()]
    if sum(lst)%2:
        print("NO")
        continue
    if lst.count(1)%2:
        print("NO")
        continue
    if lst.count(2)%2 and (1 not in lst):
        print("NO")
        continue
    print("YES")