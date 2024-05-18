n = int(input())
li = list(map(int, input().split()))

max_v = 0

for i in range(n):
    for j in range(i+2, n):
        val = 0
        val = li[i] + li[j]
        max_v = max(max_v, val)
print(max_v)