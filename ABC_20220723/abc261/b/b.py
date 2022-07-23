judge_list = [('-', '-'), ('W', 'L'), ('L', 'W'), ('D', 'D')] 

n = int(input())

a = [list(input()) for _ in range(n)]

is_correct = True

for y in range(n):
    for x in range(n):
        if not (a[y][x], a[x][y]) in judge_list:
            is_correct = False
            break           

if is_correct:
    print('correct')
else:
    print('incorrect')
