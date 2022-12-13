import sys
input = sys.stdin.readline

def dp(N, arr):          # 로직은 11722번 문제와 동일하므로 설명 생략
    dp_list = [1] * N    # dp리스트, 해당 인덱스의 값까지 만들어지는 가장 긴 수열의 길이를 담는 dp리스트
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_list[i] = max(dp_list[i], dp_list[j] + 1)
    return max(dp_list)

N = int(input())
arr = list(map(int, input().split()))
result = dp(N, arr)
print(result)