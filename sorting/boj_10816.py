import sys 
from collections import Counter

input = sys.stdin.readline

N= int(input())
arr = list(map(int, input().split()))
M= int(input())
arr1 = list(map(int, input().split()))


counter = Counter(arr)

for num in arr1:
    print(counter[num], end=' ')


#------------------------------------------------------------------#
count = {}
for card in arr:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in arr1:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")