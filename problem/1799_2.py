import sys
sys.stdin = open('1799.txt')

def find_yx(y, x, black):
    while y < N:
        while x < N:
            if visit[y][x] == 0 and arr[y][x] == 1:
                return y, x
            x += 2
        if black:
            if y % 2 == 0:
                x = 0
            else:
                x = 1
        else:
            if y % 2 == 0:
                x = 1
            else:
                x = 0
        y += 1
    return -1, -1

def check(y, x, flag):
    i = 1
    while y - i >= 0 and x - i >= 0:
        if flag:
            visit[y - i][x - i] += 1
        else:
            visit[y - i][x - i] -= 1
        i += 1

    i = 1
    while y - i >= 0 and x + i < N:
        if flag:
            visit[y - i][x + i] += 1
        else:
            visit[y - i][x + i] -= 1
        i += 1        

    i = 1
    while y + i < N and x + i < N:
        if flag:
            visit[y + i][x + i] += 1
        else:
            visit[y + i][x + i] -= 1
        i += 1

    i = 1
    while y + i < N and x - i >= 0:
        if flag:
            visit[y + i][x - i] += 1
        else:
            visit[y + i][x - i] -= 1
        i += 1


def f(y, x, cnt, black):
    global res
    if y == -1 and x == -1:
        res = max(res, cnt)
        # for i in visit:
        #     print(i)
        # print(res)
        return
    visit[y][x] += 1 
    check(y, x, 1)
    dy, dx = find_yx(y, x, black)
    f(dy, dx, cnt + 1, black)
    check(y, x, 0)
    visit[y][x] -= 1
    dy, dx = find_yx(y, x + 2, black)
    f(dy, dx, cnt, black)

N = int(input())
arr = [list(map(int, input().split())) for x in range(N)]
visit = [[0] * N for x in range(N)]
res = 0
dy, dx = find_yx(0, 0, 0)
f(dy, dx, 0, 0)
dy, dx = find_yx(0, 1, 1)
f(dy, dx, res, 1)


print(res)