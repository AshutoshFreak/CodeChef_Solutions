t = int(input())
for i in range(t):
    num = input()
    numbers = []
    for j in range(len(num)):
        n = num[:j] + num[j+1:]
        numbers.append(n)
    print(int(min(numbers)))
