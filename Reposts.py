def maxReposts(l,key,arr):
    if len(arr)==0:
        return l
    dp_arrl=[l]
    for i,pairl in enumerate(arr):
        ll = l
        if pairl[1] == key:
            ll+=1
            dp_arrl.append(maxReposts(ll, pairl[0], arr[(i + 1):]))
    return max(dp_arrl)

t = int(input())
arr = []
for i in range(t):
    s = input().split()
    if s[1] == "reposted":
        arr.append((s[0].lower(),s[2].lower()))
dp_arr = []
for i,pair in enumerate(arr):
    if pair[1] == 'polycarp':
        l = 2
        dp_arr.append(maxReposts(l,pair[0],arr[(i+1):]))
print(max(dp_arr))
