# BOJ 2720
import timeit

start_time = timeit.default_timer()
T = int(input())

for _ in range(T):
    C = int(input())

    a = C // 25
    b = (C % 25) // 10
    c = ((C % 25)% 10)//5
    d = (((C % 25)% 10)% 5)//1

    print(a,b,c,d)
terminate_time = timeit.default_timer()
terminate_time = terminate_time - start_time

print(terminate_time)
