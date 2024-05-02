n = int(input())
arr = list(map(int, input().split()))

min_val = 1e15
# 이동거리는 나의 값 * 나랑 i의 거리
for i in range(n):
    # i는 모이는 집
    tmp = 0
    for j in range(n):
        tmp += arr[j] * abs(i-j)
    
    min_val = min(tmp, min_val)

print(min_val)