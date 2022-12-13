import sys
input = sys.stdin.readline

# 문제 풀이 아이디어
# index 0부터 인덱스마다 해당 자리까지 증가하는 부분수열의 길이를 구한다.
# index n - 1부터 뒤쪽에서 인덱스마다 해당 자리까지 증가하는 부분수열의 길이를 구한다.
# 두 dp리스트를 하나로 합치고 제일 큰 값을 출력하도록 한다.

def dp(N, arr):
    dp_forward = [1] * N    # 앞에서부터 증가하는 부분수열의 길이를 인덱스마다 구한 것
    dp_backward = [1] * N   # 뒤에서부터 증가하는 부분수열의 길이를 인덱스마다 구한 것
    dp_list = [0] * N       # 두 리스트를 더할 dp리스트, 해당 인덱스에서 만들어지는 최대 바이토닉 부분수열의 길이가 나온다.

    # 1) 앞에서부터 증가하는 부분수열의 길이를 인덱스마다 구하기
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_forward[i] = max(dp_forward[i], dp_forward[j] + 1)

    # 2) 뒤에서부터 증가하는 부분수열의 길이를 인덱스마다 구하기
    for k in range(N - 1, -1, -1):
        for l in range(N - 1, k, -1):
            if arr[k] > arr[l]:
                dp_backward[k] = max(dp_backward[k], dp_backward[l] + 1)

    # 3) 두 리스트를 더해서 해당 인덱스에 만들어지는 최대 바이토닉 부분수열의 길이 구하기
    for z in range(N):
        dp_list[z] = dp_forward[z] + dp_backward[z] - 1 # -1해주는 이유: 해당 인덱스에서 하나가 겹치기 때문에

    return max(dp_list)

N = int(input())
arr = list(map(int, input().split()))
result = dp(N, arr)
print(result)
