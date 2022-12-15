import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr1 = [0] * N
arr2 = [0] * N
arr3 = [[[0] for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr1[i] = list(map(int, input().split()))

for j in range(N):
    arr2[j] = list(map(int, input().split()))

for k in range(N):
    for l in range(M):
        arr3[k][l] = arr1[k][l] + arr2[k][l]

for k in range(N):
    for l in range(M - 1):
        print(arr3[k][l], end=' ')
    print(arr3[k][-1])