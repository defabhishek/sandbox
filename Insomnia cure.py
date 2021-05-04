arr = []
for i in range(4):
    arr += [int(input())]
d = int(input())
count = 0
for i in range(1,d+1):
    for j in range(4):
        if i%arr[j] == 0:
            count += 1
            break
print(count)