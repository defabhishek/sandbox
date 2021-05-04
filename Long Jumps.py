# For example, if n=5 and a=[7,3,1,2,3], then the following game options are possible:
#
# Polycarp chooses i=1. Game process: i=0⟶+77. The score of the game is: a1=7.
# Polycarp chooses i=2. Game process: i=1⟶+34⟶+38. The score of the game is: a2+a5=6.
# Polycarp chooses i=3. Game process: i=2⟶+13⟶+25. The score of the game is: a3+a4=3.
# Polycarp chooses i=4. Game process: i=3⟶+25. The score of the game is: a4=2.
# Polycarp chooses i=5. Game process: i=4⟶+37. The score of the game is: a5=3.

T = int(input())
while T>0:
    T-=1
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    l = len(arr)-1
    dp_array = [arr[l]]
    while l>0:
        l-=1
        dp_array.append(arr[l])
        if (arr[l] + l)<len(arr):
            dp_array[-1] += dp_array[len(dp_array)-1-arr[l]]
    print(max(dp_array))