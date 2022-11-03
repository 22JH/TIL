import sys
sys.stdin = open('15865.txt')

def ft_dir(d):
    if d == 0:
        return 0, 1

    elif d == 1:
        return -1, 0

    elif d == 2:
        return 0, -1

    elif d == 3:
        return 1, 0

N = int(input())
arr = [[0] * 101 for x in range(101)]
drg = [list(map(int, input().split())) for x in range(N)] # x, y, d: 시작방향, g: 세대
cnt = 0

for i in range(N):
    x, y, d, g = drg[i]
    arr[y][x] = 1
    dir = [d]
    g = 2 ** g

    for j in range(g):
        yy, xx = ft_dir(dir[j])
        dy = y + yy
        dx = x + xx
        arr[dy][dx] = 1
        if len(dir) <= g:
            for k in range(len(dir) - 1, -1, -1):
                dir += [(dir[k] + 1) % 4]
        y = dy
        x = dx
    
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1] == 1:
            cnt += 1
print(cnt)