import math
import time
import sys


def push(x):
    a.append(x)

def pop():
    if not a:
        return -1
    else:
        return a.pop()

def size():
    return len(a)

def empty():
    if not a:
        return 1
    else:
        return 0

def top():
    return a[-1] if a else -1

num = int(sys.stdin.readline().rstrip())
a = []


for _ in range(num):
    input_split = sys.stdin.readline().rstrip().split()

    com = input_split[0]

    if com == 'push':
        push(input_split[1])
    elif com == 'top':
        print(top())
    elif com == 'size':
        print(size())
    elif com == 'pop':
        print(pop())
    elif com == 'empty':
        print(empty())

