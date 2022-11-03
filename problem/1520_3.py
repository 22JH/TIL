import sys
sys.stdin = open('1520.txt')

def f():
    global res
    q = [[arr[0][0], 0, 0]]
    visit[0][0] = 1
    while (q):
        q.sort(reverse=True)
        num, y, x = q.pop(0)
        if y == M - 1 and x == N - 1:
            continue
        for yy, xx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dy = y + yy
            dx = x + xx
            if 0 <= dy < M and 0 <= dx < N and arr[y][x] > arr[dy][dx]:
                if visit[dy][dx] == -1:
                    q.append([arr[dy][dx], dy, dx])
                    visit[dy][dx] = visit[y][x]
                else:
                    visit[dy][dx] += visit[y][x]

M, N = map(int, input().split()) # N 가로 M 세로
arr = [list(map(int, input().split())) for x in range(M)]
INF = 10e9
visit = [[-1] * N for x in range(M)]
res = 0
f()
if visit[N - 1][M - 1] == -1:
    print(0)
else:
    print (visit[N - 1][M - 1])