# Fully Correct
from math import ceil

t = int(input())
for i in range(t):
    d = int(input())
    s = input()
    actual_presence = s.count('P')
    days_of_presence = actual_presence
    for c in range(2, d-2):
        if s[c] == 'A':
            if ('P' in s[c-2:c]) and ('P' in s[c+1:c+3]):
                days_of_presence += 1
    if days_of_presence/d >= 0.75:
        required = ceil(d*0.75)
        if required > actual_presence:
            print(required-actual_presence)
        else:
            print(0)
    else:
        print(-1)
