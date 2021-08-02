import timeit
# # BOJ 10162

# T = int(input())

# if T % 10 != 0:
#     print(-1)

# else:
#     a = T // 300
#     b = (T % 300)//60
#     c=  ((T % 300)% 60) // 10
#     print(a,b,c)

# # BOJ 2720

# start_time = timeit.default_timer()
# T = int(input())

# for _ in range(T):
#     C = int(input())

#     a = C // 25
#     b = (C % 25) // 10
#     c = ((C % 25)% 10)//5
#     d = (((C % 25)% 10)% 5)//1

#     print(a,b,c,d)
# terminate_time = timeit.default_timer()
# terminate_time = terminate_time - start_time

# print(terminate_time)