# N 받는다
# N 만큼의 인원수를 받는다
# 시작하는 숫자를 변경해 가며 계산을 해준다
# min값을 구해줌

graph = []
n = int(input())
for i in range(n):
    graph.append(int(input()))

l = []
for i in range(n):
    # i는 시작하는 번호
    min_val = 1e15
    val = 0
    for j in range(i, n+i):
        if j >= n:
            val += (j-i) * graph[j-n]
        else:
            val += (j-i) * graph[j]
    l.append(val)
    
print(min(l))