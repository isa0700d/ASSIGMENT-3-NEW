n = int(input())
found = False

for i in range(n):
    x = int(input())
    if x == 0:
        found = True

if found:
    print("YES")
else:
    print("NO")