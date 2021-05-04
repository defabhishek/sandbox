n = int(input())
lst = [int(x) for x in input().strip().split()]
dparray,c = [0],0
for i,ele in enumerate(lst):
    dparray[c] += 1
    try:
        if lst[i+1] <= ele:
            dparray.append(0)
            c += 1
    except:
        break
print(max(dparray))