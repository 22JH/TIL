import sys
sys.stdin = open('bus.txt')

T = int(input())

for i in range(T):
    charge_arr = list(map(int, input().split()))
    install_arr = list(map(int, input().split()))

    bus = 0
    cnt = 0
    while bus + charge_arr[0] < charge_arr[1]:
        for j in range(charge_arr[0], 0, -1):
            if bus + j in install_arr:
                cnt += 1
                bus += j
                break
        else:
            print(f'#{i + 1} 0')
            break
    else:
        print(f'#{i + 1} {cnt}')