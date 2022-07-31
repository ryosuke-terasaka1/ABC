n, m = map(int, input().split())

dic = {}

for i in range(1, n+1):
    dic[i] = []

for _ in range(m):
    u, v = map(int, input().split())
    dic[u].append(v)

ans = 0

for k, v in dic.items():
    for b_num in v:
        for c_num in dic[b_num]:
            if c_num in v:
                ans += 1

print(ans)
