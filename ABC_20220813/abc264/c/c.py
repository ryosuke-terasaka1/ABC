import itertools
import copy

h_1, w_1 = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h_1)]

h_2, w_2 = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(h_2)]

h_d, w_d = h_1-h_2, w_1-w_2

is_convert = False

for h_list in itertools.combinations(range(h_1), h_d):
    for w_list in itertools.combinations(range(w_1), w_d):
        a_copy = copy.deepcopy(a)
        # print(h_list, w_list)
        # print(a_copy)
        for h in reversed(h_list):
            del a_copy[h]
        for w in reversed(w_list):
            for row in a_copy:
                del row[w]

        if a_copy == b:
            is_convert = True
            break

if is_convert:
    print('Yes')
else:
    print('No')




# h_c, w_c = 0, 0

# is_convert = True

# pr_h = []
# pr_w = []

# if a==b:
#     is_convert = True

# for y_2 in range(h_2):
#     for y_1 in range(h_1):
#         if set(b[y_2]) in set(a[y_1]):
#             h_c += 1
#             for x_2 in range(h_2):
#                 for x_1 in range(w_1):
#                     if a[y_1][x_1] == b[y_2][x_2]:
#                         print(x_1, y_1)
#                         if len(pr_w) < w_2:
#                             pr_w.append(x_1)
#                         else:
#                             if x_1 not in pr_w:
#                                 pr_w = []
#                                 h_c = 0            
#         else: is_convert = False

# if not(len(pr_w) == w_2 and h_c == h_2):
#     is_convert = False

# if is_convert:
#     print('Yes')
# else: print('No')

