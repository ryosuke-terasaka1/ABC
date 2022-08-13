r, c = map(int, input().split())

if r % 2 == 0:
    if min(r, 16-r) <= c <= max(r, 16-r):
        print('white')
    else: 
        if c % 2 == 0: print('white')
        else: print('black')
else:
    if min(r, 16-r) <= c <= max(r, 16-r):
        print('black')
    else: 
        if c % 2 == 0: print('white')
        else: print('black')