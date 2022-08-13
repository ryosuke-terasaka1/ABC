s = list(input())

num = 100000000000

goal = list('atcoder')
count = 0

while s != goal:
    for i in range(len(s)):
        if goal[i] == s[i]:
            continue
        else:
            index = s.index(goal[i])
            while index > i:
                s[index], s[index-1] = s[index-1], s[index]
                index -= 1
                count += 1

print(count)



