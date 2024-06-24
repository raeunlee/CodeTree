n, h, t = map(int, input().split())
arr = list(map(int, input().split()))
ans = 10000
# t번 이상이므로
for i in range(n-t+1):
    now = arr[i:i+t]
    #print(now)
    tmp_cnt = 0 
    for n in now:
        tmp_cnt += abs(h-n)
    ans = min(ans, tmp_cnt)
print(ans)