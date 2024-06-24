n, k = map(int, input().split())

l = list(map(int, input().split()))


ans = 0
for i in range(n-k+1):
    tmp = 0
    for j in range(i, i+k):
        tmp += l[j]
        ans = max(ans, tmp)

print(ans)