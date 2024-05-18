n = int(input())

graph = []
for i in range(n):
    a, b = map(int, input().split())
    graph.append([a,b])

min_dis = 1e15 #최단거리

for i in range(1, n-1):
    dis = 0 
    prev = 0
    for j in range(1,n):
        if i == j: # 건너뛰는 것과 같은 인덱스면? 
            continue # 무시
        #그렇지 않다면 전에꺼랑 계산해주기
        dis += abs(graph[prev][0] - graph[j][0]) + abs(graph[prev][1] - graph[j][1])
        prev = j #인덱스 바꿔주기

    min_dis = min(min_dis, dis)

print(min_dis)