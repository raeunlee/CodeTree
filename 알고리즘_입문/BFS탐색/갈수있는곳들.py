from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
point = [list(map(int, input().split())) for _  in range(k)]
visited = [[False] * n for _ in range(n)]
ans = 0 
# point의 개수만큼 수행한다
for i in range(len(point)):
    q = deque()
    # 출발하는 좌표를 넣어준다
    y = point[i][0] - 1
    x = point[i][1] - 1

    if not visited[y][x]:
        q.append([y,x])
        visited[y][x] = True
        ans += 1
        #print("시작좌표", y,x)
    

    dx = [0, 0, 1, -1]
    dy = [1,-1, 0, 0]

    while q:
        nowy, nowx = q.popleft() #지금 좌표

        # 0만 갈 수 있음
        for i in range(4):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] == 0 and not visited[ny][nx]:
                #print("방문하는 좌표", ny, nx)
                ans += 1
                q.append([ny,nx])
                visited[ny][nx] = True

print(ans)