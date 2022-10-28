import sys


import sys
sys.stdin = open('4340.txt')

def dfs(dir, y, x, cnt): # dir 0 : 왼쪽 // 1 : 오른쪽 // 2 : 위 // 3: 아래
    global res, flag
    if res < cnt:
        flag = 0 # 상관없음
        return
    if y == 0 and x == -1 and res >= cnt:
        flag = 0 # 상관없음
        res = cnt
        return
    if y < 0 or x < 0 or y >= N or x >= N:
        flag = 0
        return
    if arr[y][x] == 0 or visit[y][x][dir] <= cnt or visit[y][x][4] == 1:
        return
    if (y) + (x) + cnt >= res:
        flag = 0 # 시간초과
        return

    temp = visit[y][x][dir]
    visit[y][x][dir] = cnt
    visit[y][x][4] = 1
    if dir == 0:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x + 1, cnt + 1)
        else:
            dfs(3, y - 1, x, cnt + 1)
            flag = 1
            dfs(2, y + 1, x, cnt + 1)

    elif dir == 1:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x - 1, cnt + 1)
        else:
            dfs(3, y - 1, x, cnt + 1)
            flag = 1
            dfs(2, y + 1, x, cnt + 1)

    elif dir == 2:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y + 1, x, cnt + 1)
        else:
            dfs(1, y, x - 1, cnt + 1)
            flag = 1
            dfs(0, y, x + 1, cnt + 1)

    elif dir == 3:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y - 1, x, cnt + 1)
        else:
            dfs(1, y, x - 1, cnt + 1)
            flag = 1
            dfs(0, y, x + 1, cnt + 1)
    # if flag:
    #     visit[y][x][dir] = 1000000
    visit[y][x][4] = 0

def dfs2(dir, y, x, cnt): # dir 0 : 왼쪽 // 1 : 오른쪽 // 2 : 위 // 3: 아래
    global res, flag
    if res < cnt:
        # flag = 0 # 상관없음
        return
    if y == N - 1 and x == N and res >= cnt:
        # flag = 0 # 상관없음
        res = cnt
        return
    if y < 0 or x < 0 or y >= N or x >= N:
        # flag = 0
        return
    if arr[y][x] == 0 or visit[y][x][dir] <= cnt or visit[y][x][4] == 1:
        return
    if (N - y) + (N - x) + cnt >= res:
        # flag = 0 # 시간초과
        return

    temp = visit[y][x][dir]
    visit[y][x][dir] = cnt
    visit[y][x][4] = 1
    if dir == 0:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs2(dir, y, x + 1, cnt + 1)
        else:
            dfs2(3, y - 1, x, cnt + 1)
            flag = 1
            dfs2(2, y + 1, x, cnt + 1)

    elif dir == 1:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs2(dir, y, x - 1, cnt + 1)
        else:
            dfs2(3, y - 1, x, cnt + 1)
            flag = 1
            dfs2(2, y + 1, x, cnt + 1)

    elif dir == 2:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs2(dir, y + 1, x, cnt + 1)
        else:
            dfs2(1, y, x - 1, cnt + 1)
            flag = 1
            dfs2(0, y, x + 1, cnt + 1)

    elif dir == 3:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs2(dir, y - 1, x, cnt + 1)
        else:
            dfs2(1, y, x - 1, cnt + 1)
            flag = 1
            dfs2(0, y, x + 1, cnt + 1)
    # if flag:
    #     visit[y][x][dir] = 1000000
    visit[y][x][4] = 0

        
for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    res = 10e9
    visit = [[[10000000, 10000000, 10000000, 10000000, 0] for x in range(N)] for x in range(N)]
    flag = 1
    dfs(1, N - 1, N - 1, 0)
    visit = [[[10000000, 10000000, 10000000, 10000000, 0] for x in range(N)] for x in range(N)]
    dfs2(0, 0, 0, 0)
    print(f'#{t} {res}')