# Incomplete
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    pens = []
    for j in range(k):
        pens.append(input())
    arr = [[0 for i in range(n)] for j in range(k)]
    arr[0][0] = 1
    # print(arr)
    for c in range(len(s)):
        for pen in range(len(pens)):
            # print(str(s[c]) + ' ' + str(pens[pen]))
            if s[c] in pens[+pen]:
                arr[pen][c] = 1

    col = 0
    count = 0
    while col < n:
        m = 0
        for j in range(k):
            if arr[j][col] == 1:
                for h in range(col, n):
                    if arr[j][h] == 0:
                        m = max(m, h - 1)
                        break
        col = m+1
        count += 1
    print(count)
