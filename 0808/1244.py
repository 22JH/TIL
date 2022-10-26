import sys
sys.stdin = open('1244.txt')

T = int(input())
switch_arr = list(map(int, input().split()))

stud_num = int(input())
for i in range(stud_num):
    gender, num = map(int, input().split())
    sym_len = 0
    temp = num

    if gender == 1:
        if switch_arr[num - 1] == 0:
            switch_arr[num - 1] = 1
        else:
            switch_arr[num - 1] = 0

        while num < T:
            num += temp
            if num < T:
                break
            if switch_arr[num - 1] == 0:
                switch_arr[num - 1] = 1
            else:
                switch_arr[num - 1] = 0
            
    else:
        i = 1
        while num + i <= T and num - i > 0 and switch_arr[num + i - 1] == switch_arr[num - i - 1]:
            sym_len += 2
            i += 1

        if sym_len == 0:
            if switch_arr[num - 1] == 0:
                switch_arr[num - 1] = 1
            else:
                switch_arr[num - 1] = 0
        else:
            for j in range(sym_len + 1):
                if switch_arr[num - (sym_len + 1) // 2 + j - 1] == 0:
                    switch_arr[num - (sym_len + 1) // 2 + j - 1] = 1
                else:
                    switch_arr[num - (sym_len + 1) // 2 + j - 1] = 0
for i in range(len(switch_arr)):
    if i % 20 == 0 and i != 0:
        print()
    print (switch_arr[i], end=' ')    