import sys 

input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int,input().split())))
j=0
for i in range(len(arr)):
    for k in range(i+1):
        j += arr[k]

print(j)
