import sys
input = sys.stdin.readline

A, B = map(int, input().split())
result = (A + B) * (A - B)
print(result)