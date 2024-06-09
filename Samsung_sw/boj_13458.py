import math
N = int(input())
maps = list(map(int, input().split()))
B, C =  map(int, input().split())

cnt = 0
for i in maps:
    i -= B
    cnt += 1
    if i > 0:
        cnt += math.ceil(i/C)

print(cnt)

    