# Uses python3

n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    pairs = []
    for j in range(m):
        pairs.append(list(map(int, input().split())))
    employees = [False]*n
    count = []
    for j in range(m-1, -1, -1):
        if (not employees[pairs[j][0]]) and (not employees[pairs[j][1]]):
            employees[pairs[j][0]] = True
            employees[pairs[j][1]] = True
            count.append(j)
    for j in range(len(count)-1, -1, -1):
        print(count[j], end=' ')
    print()
