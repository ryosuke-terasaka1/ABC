n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
ans = 0

for i in range(n):
    if a[i] == i+1:
        b += 1
    elif i+1 == a[a[i]-1]:
        c += 0.5
print(int(b*(b-1) // 2 + c))