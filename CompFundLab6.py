from itertools import combinations

SCORES = [40,91,85,15]

pair = list(combinations(SCORES, 2))

for i in pair:
    print(f"{i[0]}" + "," + f'{i[1]}')
