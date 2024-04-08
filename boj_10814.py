import sys
input = sys.stdin.readline

n = int(input())
b = []
for _ in range(n):
    age, name = input().split()
    b.append([int(age), name])

a = sorted(b, key=lambda x:x[0])

for i in a:
    print(i[0], i[1])

    