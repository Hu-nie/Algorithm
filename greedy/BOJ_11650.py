import sys
from math import gcd

n = sys.stdin.readline().rstrip().split()

print(gcd(int(n[0]), int(n[1])))
print(int(n[0])*int(n[1])//gcd(int(n[0]), int(n[1])))




