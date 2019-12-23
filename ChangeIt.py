t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    res = max(set(s), key=s.count)
    print(n-s.count(res))
