T = int(input())

for i in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = 0

    for j in range(N):
        count = 0
        for k in range(j + 1, N):
            if arr[j] > arr[k]:
                count += 1

        if count > max_num:
            max_num = count

    print(f'#{i} {max_num}')