arr = [int(n) for n in input().strip().split("+")]
arr.sort()
print("+".join([str(n) for n in arr]))