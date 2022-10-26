T = int(input())

for i in range(T):
    num = int(input())
    
    arr = [0] * 12

    for j in range(6):
        arr[num % 10] += 1
        num //= 10
    
    k = triple = run = 0

    while k < 10:
        if arr[k] >= 3:
            arr[k] -= 3
            triple += 1
            continue

        if arr[k] and arr[k + 1] and arr[k + 2]:
            arr[k] -= 1
            arr[k + 1] -= 1
            arr[k + 2] -= 1
            run += 1
            continue
        k += 1
    
    if triple + run == 2:
        print (f'#{i + 1} 1')
    else:
        print (f'#{i + 1} 0')