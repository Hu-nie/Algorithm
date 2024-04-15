import sys
T = int(input())

data=[]
for _ in range(T):   
    arr = list(map(int, sys.stdin.readline().split()))
    data.append(arr)

for i in sorted(data,key=lambda x : (x[1], x[0])):
    print(i[0],i[1])

#------------------------------------------------------------------#
# import sys

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left, equal, right = [], [], []

#     for point in arr:
#         if point[1] < pivot[1] or (point[1] == pivot[1] and point[0] < pivot[0]):
#             left.append(point)
#         elif point[1] == pivot[1] and point[0] == pivot[0]:
#             equal.append(point)
#         else:
#             right.append(point)

#     return quick_sort(left) + equal + quick_sort(right)

# T = int(input())

# data = []
# for _ in range(T):
#     x, y = map(int, sys.stdin.readline().split())
#     data.append((x, y))

# sorted_data = quick_sort(data)

# for point in sorted_data:
#     print(point[0], point[1])