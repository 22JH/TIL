import sys
sys.stdin = open('4340.txt')

def dfs(dir, y, x, cnt): # dir 0 : 왼쪽 // 1 : 오른쪽 // 2 : 위 // 3: 아래
    global res
    if y == N - 1 and x == N - 1 and res > cnt:
        res = cnt
        return
    if y < 0 or x < 0 or y >= N or x >= N or arr[y][x] == 0 or visit[y][x] <= cnt:
        return
    temp = visit[y][x]
    visit[y][x] = cnt
    if dir == 0:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x + 1, cnt + 1)
            visit[y][x] = temp
        else:
            dfs(2, y + 1, x, cnt + 1)
            visit[y][x] = temp
            dfs(3, y - 1, x, cnt + 1)
            visit[y][x] = temp

    elif dir == 1:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y, x - 1, cnt + 1)
            visit[y][x] = temp
        else:
            dfs(2, y + 1, x, cnt + 1)
            visit[y][x] = temp
            dfs(3, y - 1, x, cnt + 1)
            visit[y][x] = temp

    elif dir == 2:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y + 1, x, cnt + 1)
            visit[y][x] = temp
        else:
            dfs(0, y, x + 1, cnt + 1)
            visit[y][x] = temp
            dfs(1, y, x - 1, cnt + 1)
            visit[y][x] = temp

    elif dir == 3:
        if arr[y][x] == 1 or arr[y][x] == 2:
            dfs(dir, y - 1, x, cnt + 1)
            visit[y][x] = temp
        else:
            dfs(0, y, x + 1, cnt + 1)
            visit[y][x] = temp
            dfs(1, y, x - 1, cnt + 1)
            visit[y][x] = temp

for t in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for x in range(N)]
    visit = [[10000] * N for x in range(N)]
    res = 10e9
    dfs(0, 0, 1, 1)
    print(res)