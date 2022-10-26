import sys
sys.stdin = open('input (3).txt')

def max_num(*arr):
    res = 0
    for i in arr:
        if i > res:
            res = i
    return res

for i in range(10):
    num = int(input())
    arr = [list(map(int, input().split())) for x in range(100)]

    total_num = 0
    res = 0

    for j in range(100):
                
        col_sum = 0
        row_sum = 0
        div_sum = 0
        div_reverse_sum = 0

        for k in range(100):
            row_sum += arr[j][k]
            col_sum += arr[k][j]
            if j == 0:
                div_sum += arr[k][k]
                div_reverse_sum += arr[k][99 - k]
        total_num = max_num(col_sum, row_sum, div_sum, div_reverse_sum)
        if res < total_num:
            res = total_num

    print(f'#{i + 1} {res}')