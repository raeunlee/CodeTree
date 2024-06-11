# 적어도 한 칸 이상 오른쪽 + 한 칸 이상 아래쪽 -> x + n, y + m 로 이동
# 시작, 도착 지점을 제외하고 2곳만 들려야 함 
r, c = map(int, input().split())
# 체크판 받기
arr = []
for _ in range(r):
    row = list(input().split())
    arr.append(row)

# 행과 열이 전부 증가하도록 모든 쌍을 다 탐색

cnt = 0 

# (1,1) 부터 도착 지점까지 탐색했을때 들르는 2지점이 모두 다른 경우를 다 세준다
for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[r-1][c-1]:
                    cnt += 1

print(cnt)