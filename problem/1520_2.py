import sys
import heapq
sys.stdin = open('1520.txt')

def f():
    global res
    heap_list = [[0, 0]]
    # q = [[0, 0]]
    visit[0][0] = 1
    while (heap_list):
        y, x = heap_list.heapop()
        if y == M - 1 and x == N - 1:
            continue
        for yy, xx in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dy = y + yy
            dx = x + xx
            if 0 <= dy < M and 0 <= dx < N and arr[y][x] > arr[dy][dx]:
                
                q.append([dy, dx])
                if visit[dy][dx] == -1:
                    visit[dy][dx] = 0

                visit[dy][dx] += visit[y][x]

M, N = map(int, input().split()) # N 가로 M 세로
arr = [list(map(int, input().split())) for x in range(M)]
INF = 10e9
visit = [[-1] * N for x in range(M)]
res = 0
f()
print (visit)