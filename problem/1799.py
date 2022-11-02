import sys
sys.stdin = open('1799.txt')

def max_b(y, x, cnt):
    global res
    while y < N:
        while x < N:
            if arr[y][x] == 1:
                cnt += 1
            x += 1
        x = 0
        y += 1
    if res >= cnt:
        return 1

def is_valid(y, x):
    i = 1
    while y - i >= 0 and x - i >= 0:
        if visit[y - i][x - i] == 1:
            return 0
        i += 1

    i = 1
    while y - i < N and x + i < N:
        if visit[y - i][x + i] == 1:
            return 0
        i += 1        
    return 1

def f(y, x, cnt):
    global res
    if y == N and x == 0:
        res = max(res, cnt)
        # for i in visit:
        #     print(i)
        # print(res)
        return
    if max_b(y, x, cnt):
        return
    if arr[y][x] == 1:
        if is_valid(y, x):
            visit[y][x] = 1
            if x == N - 1:
                f(y + 1, 0, cnt + 1)
            else:
                f(y, x + 1, cnt + 1)
            visit[y][x] = 0
    if x == N - 1:
        f(y + 1, 0, cnt)
    else:
        f(y, x + 1, cnt)

N = int(input())
arr = [list(map(int, input().split())) for x in range(N)]
visit = [[0] * N for x in range(N)]
res = 0

f(0, 0, 0)

print(res)