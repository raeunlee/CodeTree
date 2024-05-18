a = list(map(int, input()))

max_val = 0

for i in range(len(a)):
    # 자릿 수 바꾸기 
    a[i] = 1 - a[i]
    
    num = 0

    for j in range(len(a)):
        num = num * 2 + a[j]

    max_val = max(max_val, num)

    a[i] = 1 - a[i]

print(max_val)