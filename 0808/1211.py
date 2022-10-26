import sys
sys.stdin = open('input (3).txt')

for i in range(10):
    num = int(input())
    arr = [list(map(int, input().split())) for x in range(100)]

    y = 0
    min_cnt = 10000
    for idx, j in enumerate(arr[99]):
        if j == 1:
            y = idx
            x = 99
            flag = 0
        
            cnt = 0
            while x > 0:
                while arr[x - 1][y] != 0 and (((y == 0 or arr[x][y - 1] != 1) and (y == 99 or arr[x][y + 1] != 1)) or flag == 1 or flag == 2):
                    x -= 1
                    flag = 0
                    cnt += 1
                    if x < 0:
                        break
                while y != 0 and arr[x][y - 1] != 0:
                    if flag == 2:
                        break
                    y -= 1
                    flag = 1
                    cnt += 1
                while  y != 99 and arr[x][y + 1] != 0:
                    if flag == 1:
                        break
                    y += 1
                    flag = 2
                    cnt += 1

            if min_cnt > cnt:
                min_cnt = cnt
                res = y

    print (f'#{i + 1} {res}')