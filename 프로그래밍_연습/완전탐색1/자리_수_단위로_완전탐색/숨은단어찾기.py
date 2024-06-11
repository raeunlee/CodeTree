n, m = map(int, input().split())
words = []

# 위, 아래, 좌, 우, 우상승, 좌하향, 좌상승, 우하향
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

for i in range(n):
    tmp = list(input())
    words.append(tmp)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

ans = 0
for i in range(n):
    for j in range(m):
        if words[i][j] == 'L': 
            # L을 찾으면 8방향으로 탐색
            for k in range(8):
                # 매 방향마다 e 카운트를 0으로 초기화한 뒤 탐색한다
                found = True
                x = i
                y = j
                for _ in range(2):
                    x += dx[k]
                    y += dy[k]
                    # 범위 넘거나, E가 아니라면 break
                    if not in_range(x,y) or words[x][y] != 'E':
                        found = False
                        break
                if found:
                    ans += 1
                
                    
print(ans)