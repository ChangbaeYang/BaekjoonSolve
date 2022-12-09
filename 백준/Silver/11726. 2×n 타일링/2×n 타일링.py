import sys
input = sys.stdin.readline

# 몇가지 예시 관찰을 통해, 그리고 input의 값을 통해 피보나치 수열을 이용하는 문제임을 확인할 수 있다.
# 이 때, 피보나치 수열을 이용한 문제는 DP를 이용할 수 있음을 기억하자.
def fibo_dp(n):
    if n == 1:  # 1인 예외적인 상황처리 해준다.(예외처리)
        return 1
    cache = [0 for index in range(n + 1)]
    cache[0] = 0 # 문제조건에는 해당되지 않지만, 편하게 다루기 쉽게 하기 위해서 남겨둔다.
    cache[1] = 1
    cache[2] = 2
    for index in range(3, n + 1):
        cache[index] = cache[index - 1] + cache[index - 2]
    return cache[n]

n = int(input())
result = fibo_dp(n) % 10007 # 나눈 나머지!
print(result)

