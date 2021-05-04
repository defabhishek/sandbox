# 19 28 37 46 55 64 73 82 91 109 118 127
# 11,22,33
n = int(input())
i = 9
arr = [19,28,37,46,55,64,73,82,91]
p = 2
while (n)>i:
    loc = 10**p
    for k in range(1,10):
        j = 0
        arr.append(k*loc + 10-k)
        while j <i:
            if  (arr[j]%10-k)>=0:
                arr.append(k*loc+arr[j]-k)
            j+=1
    i = len(arr)
    p+=1

print(arr[n-1])
