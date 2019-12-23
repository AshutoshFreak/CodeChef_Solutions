def xpr(n):
    n = '{0:b}'.format(n)
    m = n
    n = n[::-1]
    for k in range(len(n)):
        if n[k] == '1':
            return int((n[:k] + '0' + n[k+1:])[::-1], 2)


t = int(input())
for i in range(t):
    # l, r = map(int, input().split())
    # s = 0
    # for j in range(l, r+1):
    #     x = xpr(j)
    #     if x == 0:
    #         x = -1
    #     s += x
    n = int(input())
    for j in range(n):
        print(str(j) + ' ' + str(xpr(j)))
    # print(s)
