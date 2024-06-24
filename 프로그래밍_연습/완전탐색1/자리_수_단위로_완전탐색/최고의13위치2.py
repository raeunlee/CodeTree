n = int(input())

arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

max_cnt = 0

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                # 첫번쨰 놓는것 위치 i,j 두번째 k,l 
                # 같은행이고 겹칠때는 제외해줌
                if i == k and abs(j-l) <= 2:
                    continue
                
                cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]

                max_cnt = max(max_cnt, cnt1+cnt2)
print(max_cnt)