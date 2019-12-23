t = int(input())
for i in range(t):
    n = int(input())
    scores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
    for j in range(n):
        problem, score = map(int, input().split())
        scores[problem] = max(scores[problem], score)
    # print(scores)
    total = sum(scores.values()) - scores[9] - scores[10] - scores[11]
    print(total)
