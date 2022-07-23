n, k, q = map(int, input().split())

a = list(map(int, input().split()))

l = list(map(int, input().split()))

n_list = [0 for _ in range(n)]

for i in range(k):
    n_list[i] = a[i]

for l_value in l:
    index = 0
    for i in range(n):
        if n_list[i] != 0:
            index += 1
        if index == l_value:
            if i == n-1:
                continue
            else:
                if n_list[i+1]:
                    continue
                else:
                    n_list[i], n_list[i+1] = n_list[i+1], n_list[i]

result = []

for i in range(n):
    if n_list[i]:
        result.append(i)

print(*result)