#import sys
#sys.stdin = open('input.txt')

T = 10
def min_num(*arr):
    res = 1000
    for i in arr:
        if i < res:
            res = i
    return res

for i in range(T):

    num = int(input())
    arr = list(map(int, input().split()))   

    tower = 0

    res = 0
    for j in range(2, num - 1):
        if arr[j] > arr[j - 1] and arr[j] > arr[j + 1] and arr[j] > arr[j - 2] and arr[j] > arr[j + 2]:
            res_1 = arr[j] - arr[j - 1]
            res_2 = arr[j] - arr[j + 1]
            res_3 = arr[j] - arr[j - 2]
            res_4 = arr[j] - arr[j + 2]

            res += min_num(res_1, res_2, res_3, res_4)

    print (f'#{i + 1} {res}')        