import sys
sys.stdin = open('1520.txt')

def f(y, x):
    global res, flag, INF
    temp.append([y, x])
    if y == M - 1 and x == N - 1:
        flag = 0
        res += 1
        # visit[y][x] = 1
        for y, x in temp:
            visit[y][x] = 1
        return
    if y < 0 and y >= N and x < 0 and x >= N:
        return
    # visit[y][x] = 1
    for yy, xx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        dy = y + yy
        dx = x + xx
        if dy == M - 1 and xx == -1:
            continue
        if dx == N - 1 and yy == -1:
            continue
        if 0 <= dy < M and 0 <= dx < N and arr[y][x] > arr[dy][dx]:
            flag = 1
            if visit[dy][dx] == 0:
                f(dy, dx)
            else:
                res += 1
    temp.pop()
            #     flag = 0
            # if flag:
            #     visit[dy][dx] = 0

M, N = map(int, input().split()) # N 가로 M 세로
arr = [list(map(int, input().split())) for x in range(M)]
INF = 10e9
visit = [[0] * N for x in range(M)]
res = 0
flag = 1
temp = []
f(0, 0)
print (res)