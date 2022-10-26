import sys
sys.stdin = open('input1.txt')

for i in range(10):
    num = int(input())
    arr = [list(map(int, input().split())) for x in range(100)]

    y = 0
    for idx, j in enumerate(arr[99]):
        if j == 2:
            y = idx
    x = 99
    flag = 0

    while x > 0:
        while arr[x - 1][y] != 0 and (((y == 0 or arr[x][y - 1] != 1) and (y == 99 or arr[x][y + 1] != 1)) or flag == 1 or flag == 2):
            x -= 1
            flag = 0
            if x < 0:
                break
        while y != 0 and arr[x][y - 1] != 0:
            if flag == 2:
                break
            y -= 1
            flag = 1
        while  y != 99 and arr[x][y + 1] != 0:
            if flag == 1:
                break
            y += 1
            flag = 2       
                
    print (f'#{i + 1} {y}')