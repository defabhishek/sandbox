t,s = map(int,input().strip().split())
lily = [int(x) for x in input()]
l = len(lily)
ptr,jmp = 0,0
while 1:
    flag = 0
    for i in range(s,0,-1):
        try:
            if lily[ptr+i]:
                jmp += 1
                ptr = ptr+i
                flag = 1
                break
        except:
            continue
    if ptr == (l-1):
        print(jmp)
        break
    if not flag:
        print(-1)
        break