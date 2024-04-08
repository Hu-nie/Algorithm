from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))

max_combo = 0
for combo in combinations(card, 3):
    temp = sum(combo)

    if M >= temp and max_combo <= temp:
        max_combo = temp

print(max_combo)