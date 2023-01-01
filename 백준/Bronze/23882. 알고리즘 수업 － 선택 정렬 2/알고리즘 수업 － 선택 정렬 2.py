import sys
input = sys.stdin.readline

def selection_sort(N, A, K):
    count = 0
    for i in range(N - 1, 0, -1):
        max_value = max(A[:i + 1])
        max_index = A.index(max_value)
        if max_value > A[i]:    # 만약 마지막 값보다 범위 내 최댓값이 크다면 교체
            A[max_index], A[i] = A[i], A[max_index]
            count += 1
        if count == K:
            return A
    return -1

N, K = map(int, input().split())        # N: 배열의 크기(5이상 10,000이하), K: 교환 횟수(1이상 N이하)
A = list(map(int, input().split()))     # 배열, 하나의 원소는 1이상 10**9 이하

# 구하고자 하는 것 : K번 교환 발생후 배열 A
# 만약 K번이 완전히 최대 교환횟수보다 크다면 -1을 출력한다.
result = selection_sort(N, A, K)
if result == -1:
    print(-1)
else:
    for i in range(len(result) - 1):
        print(result[i], end= ' ')
    print(result[-1])

