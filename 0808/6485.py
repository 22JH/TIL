T = int(input())

for i in range(T):
    N = int(input()) # 버스 노선 개수

    arr = [0] * 5000
    for j in range(N):
        A, B = map(int, input().split())

        for k in range(A - 1, B):
            arr[k] += 1
    P = int(input())
    print(f'#{i + 1} ', end ='')
    for j in range(P):
        C = int(input())
        print(arr[C - 1], end = ' ')
    print()
    