n = int(input())

p = list(map(int, input().split()))

p_dic = {}


for j in range(2, n+1):
    p_dic[j] = p[j-2]


count = 0

num = n

while num != 1:
    num = p_dic[num]
    count += 1

print(count)
