n, m = map(int, input().split())
x = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]
bonus = [0] * (n+1)

for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i][j]=dp[i-1][j-1]+x[i-1]+bonus[j]
    dp[i][0] = max(dp[i-1])

print(max(dp[n]))