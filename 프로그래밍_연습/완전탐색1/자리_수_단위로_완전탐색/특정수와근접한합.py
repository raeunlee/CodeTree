
n, s = map(int, input().split())
l = list(map(int, input().split()))

min_val = 1e15

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        tmp = sum(l) - (l[i] + l[j])
        minus = abs(s - tmp)
        min_val = min(min_val, minus)

print(min_val)