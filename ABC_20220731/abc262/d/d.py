n = int(input())

a = list(map(int, input().split()))

ans = 0


for j in range(1, 2**n):
    sum_num = 0
    str_num = format(j, 'b')
    str_num = '0'*(n-len(str_num)) + str_num
    one_num = sum(map(int, str_num))
    for i in range(n):
        if str_num[i] == '1': sum_num += a[i]
    if sum_num % one_num == 0:
        ans += 1

print(ans % 998244353)
