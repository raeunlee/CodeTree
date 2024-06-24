import sys

arr = []
for i in range(19):
    row = list(map(int, input().split()))
    arr.append(row)

# 위, 아래, 좌, 우, 우상승, 좌 하향, 좌상승, 우하향 -> 8가지 방향
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, -1, 1]

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue
        for d in range(8):
            cnt = 1
            nx, ny = i, j
            while True:
                nx += dx[d]
                ny += dy[d]
                # 범위를 넘어서거나, 직전의 돌과 다르다면?
                if not in_range(nx, ny) or arr[nx][ny] != arr[i][j]:
                    break
                cnt += 1

            if cnt == 5:
                print(arr[i][j])
                print(i + 2 * dx[d] + 1, j + 2 * dy[d] + 1)
                sys.exit()

print(0)
