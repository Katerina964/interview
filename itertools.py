from itertools import groupby, permutations
from collections import defaultdict, Counter

print(list(permutations('123', 2)))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

grouper = lambda item: item['country']
data = [
    {'city': 'Москва', 'country': 'Россия'},
    {'city': 'Новосибирск', 'country': 'Россия'},
    {'city': 'Пекин', 'country': 'Китай'},
]
for key, group in groupby(data, key=grouper):
    print(key, *group)

cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(cnt)
print(dict(cnt))

# вывод:
# Counter({'blue': 3, 'red': 2, 'green': 1})
# {'red': 2, 'blue': 3, 'green': 1}


d = defaultdict(int)
print(d['apple'])

d = defaultdict(list)
print(d['apple'])

d = defaultdict(set)
print(d['apple'])

# вывод:
# 0
# []
# set()    