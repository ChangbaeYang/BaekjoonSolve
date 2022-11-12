import sys
input = sys.stdin.readline
arr = [i for i in range(1, 31)]
for i in range(28):
    a = int(input())
    if a in arr:
        arr.remove(a)
for j in range(2):
    print(arr[j])