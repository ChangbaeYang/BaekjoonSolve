import sys
input = sys.stdin.readline

def dp(arr):
    dp = [1] * N    # 최소 1만큼의 수열의 길이는 나오기 때문이다.

    for i in range(1, N):       # 다음 요소들을 순회한다.
        for j in range(i):      # 다음 요소의 전까지의 요소들을 순회한다.
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

N = int(input())    # 1 <= N <= 1000
arr = list(map(int, input().split()))   # 원소 Ai가 들어간다. 1 <= Ai <= 1000
result = dp(arr)
print(result)