n, m = map(int, input().split())

x = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = x[0]
bonus_dic = {}
bonus_sum = 0

for _ in range(m):
    c, y = map(int, input().split())
    bonus_dic[c] = y
    bonus_sum += y

for i in range(1, n):
    for k, v in bonus_dic.items():
        if i == k:
            dp[i] = max(dp[i-1]+x[i], x[i]+v, dp[i])
        elif i > k > 1:
            dp[i] = max(dp[i-k-1]+sum(x[i-k+1:i+1])+v, dp[i], dp[i-1]+x[i]+bonus_sum)
        else:
            dp[i] = max(dp[i-1]+x[i], dp[i])
print(max(dp[n-1], (bonus_sum+sum(x))))