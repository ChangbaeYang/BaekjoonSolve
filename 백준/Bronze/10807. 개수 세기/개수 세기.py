import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))
n = int(input())
result = 0
for i in range(T):
    if arr[i] == n:
        result += 1
print(result)
        