# Partially correct
from math import floor

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    r = (1-k+n)//(1-n) + 2
    ans = r*(k+n-1) - r*(r+1)*(n-1)//2 - r
    ans = pow(ans, 1, 1000000007)
    print(ans)
