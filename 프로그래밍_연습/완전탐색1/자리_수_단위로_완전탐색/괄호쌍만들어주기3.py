l = input()
length = len(l)

count = 0
for i in range(length):
    if l[i] == '(':
        for j in range(i, length):
            if l[j] == ")":
                count += 1
print(count)