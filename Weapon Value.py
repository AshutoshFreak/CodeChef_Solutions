t = int(input())
for i in range(t):
    s = []
    n = int(input())
    for j in range(n):
        s.append(int(input(), 2))
    ans = 0
    for number in s:
        ans = ans ^ number
    print('{0:b}'.format(ans).count('1'))
