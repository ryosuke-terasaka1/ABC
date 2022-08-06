import itertools

n, m = map(int, input().split())

for ans in itertools.combinations(range(1, m+1), n):
    print(*ans)
