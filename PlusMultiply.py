t = int(input())
for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    count0 = 0
    count2 = 0
    total = 0
    for num in numbers:
        if num == 0:
            count0 += 1
        elif num == 2:
            count2 += 1
    if count0 > 1:
        total += count0*(count0-1)/2
    if count2 > 1:
        total += count2*(count2-1)/2
    print(int(total))
