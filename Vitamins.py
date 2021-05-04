import sys
min_value = sys.maxsize
def minimumPrice(arr,price=0,vitamins=""):
    global min_value
    if "A" in vitamins and "B" in vitamins and "C" in vitamins:
        if min_value > price:
            min_value = price
        return min_value
    dp_arr = [min_value]
    for i,obj in enumerate(arr):
        if obj.price + price > min_value:
            continue
        flag = 0
        for objvitamins in obj.vitamins:
            if objvitamins not in vitamins:
                flag +=1
                break
        if not flag:
            continue
        dp_arr.append(minimumPrice(arr[(i+1):],price+obj.price,vitamins+obj.vitamins))
    return min(dp_arr)
class graph():
    def __init__(self,price,vitamins):
        self.price = int(price)
        self.vitamins = vitamins
t = int(input())
arr = []
for i in range(t):
    price,vitamins=map(str,input().strip().split())
    arr.append(graph(price,vitamins))
sol = minimumPrice(arr)
if sol == sys.maxsize:
    sol =-1
print(sol)