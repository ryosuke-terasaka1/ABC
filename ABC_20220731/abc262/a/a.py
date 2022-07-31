y = int(input())

for _ in range(4):
    if y % 4 == 2:
        print(y)
        break
    else:
        y += 1
