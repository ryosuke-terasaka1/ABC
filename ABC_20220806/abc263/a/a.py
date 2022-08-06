input_list = list(map(int, input().split()))

input_list.sort()

change_list = []

correct_change = {1, 2}

for i in range(4):
    if input_list[i] != input_list[i+1]:
        change_list.append(i)

if len(change_list) == 1 and change_list[0] in correct_change: print('Yes')
else: print('No')
