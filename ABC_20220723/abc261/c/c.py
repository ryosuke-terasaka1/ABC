n = int(input())

str_set = set()
str_dic = {}

for _ in range(n):
    word = input()
    if word not in str_set:
        print(word)
        str_set.add(word)
        str_dic[word] = 1
    else:
        print(f'{word}({str_dic[word]})')
        str_dic[word] += 1
