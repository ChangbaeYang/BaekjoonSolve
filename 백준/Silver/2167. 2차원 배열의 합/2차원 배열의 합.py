import sys
input = sys.stdin.readline

def sub_sum(i, j, x, y, arr):
    result = 0      # 합이 들어갈 것
    for k in range(i - 1, x):
        for l in range(j - 1, y):
            result += arr[k][l]
    return result

N, M = map(int, input().split())    # N*M 행
arr = [0] * N   # 배열을 담을 리스트
for i in range(N):
    r = list(map(int, input().split()))     # 한 행의 정보를 받아온다.
    arr[i] = r      # 한 행을 리스트에 추가한다.

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = sub_sum(i, j, x, y, arr)
    print(result)