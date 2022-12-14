import sys
input = sys.stdin.readline

def dp(N, arr):
    dp_list = [0] * N               # dp_list는 해당 인덱스까지의 증가하는 부분수열의 합을 구한 것이다.
    for i in range(N):
        dp_list[i] = arr[i]

    # 로직은 감소하는 부분수열의 길이를 구하는 것과 같다.
    for i in range(N):              # arr의 인덱스를 순회하며 값을 찾을 것이다.
        for j in range(i):          # 해당 인덱스(i)보다 앞의 값을 순회한다.
            if arr[i] > arr[j]:     # 만약 앞의 값이 해당 인덱스보다 값이 적다면 앞의 값의 dp값에 해당 인덱스의 값을 더한다.
                dp_list[i] = max(dp_list[i], arr[i] + dp_list[j])
    return max(dp_list)


N = int(input())    # 수열의 크기 (1 <= N <= 1,000)
arr = list(map(int, input().split()))
result = dp(N, arr)
print(result)

