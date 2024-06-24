n, k = map(int, input().split())

arr = [0] * 10000

for i in range(n):
    a, b = input().split()
    x = int(a)
    if b == 'G':
        arr[x] = 1
    elif b == 'H':
        arr[x] = 2

# print(arr)

ans = 0

for i in range(1, len(arr)-k):
    tmp = 0
    for j in range(i, i+k+1):
        tmp += arr[j]
    ans = max(ans, tmp)
print(ans)