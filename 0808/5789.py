import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

for i in range(T):
    N, Q = map(int, input().split()) # N = 상자의 갯수 Q = 반복 횟수
    arr = [0] * N
    for j in range(Q):
        L, R = map(int, input().split())
        for k in range(L - 1, R):
            arr[k] = j + 1

    print (f'#{i + 1}', *arr) 