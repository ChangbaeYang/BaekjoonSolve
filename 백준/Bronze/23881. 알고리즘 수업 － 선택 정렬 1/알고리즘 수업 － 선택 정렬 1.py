import sys
input = sys.stdin.readline

def selection_sort(A, N):
    count = 0       # 교환 횟수를 체크하는 변수
    for i in range(N - 1, 0, -1):
        max_value = max(A[:i + 1])      # 가장 큰 값(범위 내)
        max_index = A.index(max_value)  # 가장 큰 값의 인덱스(범위 내)
        if max_value > A[i]:            # 만약 그 값이 마지막 인덱스보다 크다면
            A[max_index], A[i] = A[i], A[max_index] # 자리교환
            count += 1
        if count == K:          # K 만큼 교환했다면
            a = A[max_index]    # 교환 후 작은 값
            b = A[i]    # 교환 후 큰 값
            return (a, b)
    return -1


N, K = map(int, input().split())    # 5 <= N <= 10,000, 교환횟수 K(1 <= K <= N)
A = list(map(int, input().split())) # 원소 값은 10**9이하의 양의 정수
result = selection_sort(A, N)
if result == -1:
    print(-1)
else:
    a, b = result
    print(a, b)