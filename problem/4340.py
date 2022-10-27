import sys
sys.stdin = open('4340.txt')

def minf(y, x, cnt):
        global res
        if (N - y) + (N - x) + cnt >= res:
            return 1
        return 0

def dfs(dir, y, x, cnt): # dir 0 : 왼쪽 // 1 : 오른쪽 // 2 : 위 // 3: 아래
    global res, flag
    if res < cnt:
        flag = 0
        return
    if y == N - 1 and x == N and res >= cnt:
        res = cnt
        return
    if y < 0 or x < 0 or y >= N or x >= N or arr[y][x] == 0 or visit[y][x][dir] < cnt or visit[y][x][4] == 1:
        return
    if minf(y, x, cnt):
        return
    temp = visit[y][x][dir]
    visit[y][x][dir] = cnt
    visit[y][x][4] = 1
    if dir == 0:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x + 1, cnt + 1)
            if flag:
                visit[y][x][dir] = temp
        else:
            dfs(2, y + 1, x, cnt + 1)
            flag = 1
            dfs(3, y - 1, x, cnt + 1)

    elif dir == 1:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x - 1, cnt + 1)
            if flag:
                visit[y][x][dir] = temp
        else:
            dfs(2, y + 1, x, cnt + 1)
            flag = 1
            dfs(3, y - 1, x, cnt + 1)

    elif dir == 2:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y + 1, x, cnt + 1)
        else:
            dfs(0, y, x + 1, cnt + 1)
            flag = 1
            dfs(1, y, x - 1, cnt + 1)

    elif dir == 3:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y - 1, x, cnt + 1)
        else:
            dfs(0, y, x + 1, cnt + 1)
            flag = 1
            dfs(1, y, x - 1, cnt + 1)
    visit[y][x][4] = 0
    if flag:
        visit[y][x][dir] = temp
for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    res = 10e9
    visit = [[[10000000, 10000000, 10000000, 10000000, 0] for x in range(N)] for x in range(N)]
    flag = 1
    dfs(0, 0, 0, 0)
    print(f'#{t} {res}')