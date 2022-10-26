#import sys
#sys.stdin = open('input (2).txt')

T = 10

for i in range(T):
    num = int(input())
    arr = list(map(int, input().split()))    

    for k in range(num + 1):
        max_num = 0
        min_num = 1001
        max_idx = 1001
        min_idx = -1
        for x in range(len(arr)):
            if arr[x] >= max_num:
                max_num = arr[x]
                max_idx = x
            if arr[x] <= min_num:
                min_num = arr[x]
                min_idx = x
        if k != num:
            arr[max_idx] -= 1
            arr[min_idx] += 1

    print(f'#{i + 1} {max_num - min_num}')