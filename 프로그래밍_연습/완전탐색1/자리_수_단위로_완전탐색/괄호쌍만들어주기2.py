li = list(input())

cnt = 0
for i in range(len(li)):
    for j in range(i+1, len(li)-1):
        if li[i] == '(' and li[i+1] == '(' and li[j] == ')' and li[j+1] == ')':
            cnt += 1

print(cnt)