n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if arr[i] <= arr[k] <= arr[j]:
                
                #print(arr[i], arr[k], arr[j])
                count += 1
print(count)