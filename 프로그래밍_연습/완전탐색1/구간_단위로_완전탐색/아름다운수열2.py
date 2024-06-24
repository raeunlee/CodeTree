n,m  = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()

# 구간만큼 끊어준다
cnt = 0
for i in range(n-m+1):
    tmp = []
    # 이게 그 각 구간임
    for j in range(i, i+m):
        tmp.append(a[j])
    tmp.sort()
    #print(tmp)
    if tmp == b:
        cnt += 1

print(cnt)