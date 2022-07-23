l_1, r_1, l_2, r_2 = map(int, input().split())

if l_1 > l_2 and r_1 < r_2:
    ans = r_1 - l_1
elif l_1 > l_2 and r_1 >= r_2:
    ans = r_2 - l_1
    if ans < 0:
        ans = 0
elif l_1 <= l_2 and r_1 < r_2:
    ans = r_1 - l_2
    if ans < 0:
        ans = 0
else:
    ans = r_2 - l_2
    
print(ans)


