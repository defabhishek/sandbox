# 5
# 3 10 8 6 11 --> 3 6 8 10 11
# 4
# 1
# 10
# 3
# 11
s = int(input()) # number of shops
p_list = [int(x) for x in input().strip().split()] # price of bottle in each shop
p_list.sort() # nlogn
d = int(input()) # number of days
d_lst = [] # budget on each day
dp_dict = {}
for i in range(d):
    d_lst.append(int(input()))
for budget in d_lst:
    if budget >= p_list[-1]:
        print(s)
        continue
    if budget <p_list[0]:
        print(0)
        continue
    if budget in dp_dict.keys():
        print(dp_dict[budget])
        continue
    start,end,mid = 0,s-1,s//2
    while start<=mid and end>mid:
        if budget >= p_list[mid]:
            start = mid+1
        if budget < p_list[mid]:
            end = mid
        mid = (start+end)//2
    dp_dict[budget] = mid
    print(mid)