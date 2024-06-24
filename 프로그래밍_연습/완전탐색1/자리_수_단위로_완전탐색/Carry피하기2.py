n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

ans = -1

# 수 3개를 뽑으므로 3중 포문
for i in range(n):
    for j in range(i + 1 , n):
        for k in range(j + 1, n):
            carry = False

            # 일
            if arr[i] % 10 + arr[j] % 10 + arr[k] % 10 >= 10:
                carry = True
            
            # 십
            if arr[i] % 100 // 10 + arr[j] % 100 // 10 + arr[k] % 100 // 10 >= 10:
                carry = True
            
            # 백
            if arr[i] % 1000 // 100 + arr[j] % 1000 // 100 + arr[k] % 1000 // 100 >= 10:
                carry = True
            
            # 천
            if arr[i] % 10000 // 1000 + arr[j] % 10000 // 1000 + arr[k] % 10000 // 1000 >= 10:
                carry = True

            if carry == False:
                ans = max(ans, arr[i] + arr[j] + arr[k]);

print(ans)
