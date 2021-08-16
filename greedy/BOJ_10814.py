import sys

while True:
    T = list(map(int, input().split()))
    max_num = max(T)
    
    if sum(T) == 0:
        break
    T.remove(max_num)
    if (int(T[0])**2 + int(T[1])**2) == (max_num**2):
        print('right')
    else:
        print('wrong')

