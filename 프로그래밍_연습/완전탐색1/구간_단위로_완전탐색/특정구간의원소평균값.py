n = int(input())
arr = list(map(int, input().split()))

ans = 0
#구간은 1부터 n까지의 경우의 수를 가진다
for i in range(n):
    for j in range(i,n):
        tmp_sum = 0 
        for k in range(i,j+1):
            tmp_sum += arr[k]
        
        tmp_avg = tmp_sum / (j-i+1)

        exists = False
        for k in range(i, j + 1):
            if arr[k] == tmp_avg:
                exists = True
        if exists:
            ans += 1
print(ans)