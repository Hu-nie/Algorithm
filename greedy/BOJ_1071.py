n = int(input())
num = list(map(int, input().split()))

num.sort()
num = list(set(num))

print(num)
i = 0
for i in range(n-1):
    if num[i]+1 != num[i+1]:
        break

print(i)
# x =[]



# for i in range(n-1):
#     if num[i]+1 == num[i+1]:
#         x.append(num[i])

# print(x)


