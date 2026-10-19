n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        if n > 0:
            print(i, end=' ')
            n -= 1
        else:
            break
    if n == 0:
        break