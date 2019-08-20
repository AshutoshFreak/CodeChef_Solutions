# Fully Correct
t = int(input())
z = 1000000007
for i in range(t):
    k = int(input())
    print(((10 % z)*pow(2, k-1, z)) % z)
