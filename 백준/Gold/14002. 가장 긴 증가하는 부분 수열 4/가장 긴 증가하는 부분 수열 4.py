import sys
input = sys.stdin.readline

def dp(N, arr):
    dp_dict = dict()
    for i in range(N):
        dp_dict[i] = [1, [arr[i]]]  # dp_dict[i]는 i key에서 [길이, [해당 길이를 만드는 수열]]이 value로 들어갈 것이다. 길이 1은 초기값

    for j in range(N):
        for k in range(j):
            if arr[j] > arr[k]:
                dp_dict[j][0] = max(dp_dict[j][0], dp_dict[k][0] + 1)   # 길이가 변경되는지를 확인
            if dp_dict[j][0] == dp_dict[k][0] + 1:   # 길이 변경이 일어났거나 그대로 유지된다면(유지되더라도 수열이 변경되는 것은 상관없다. *아무거나)
                # dp_dict[j][1] = dp_dict[k][1].append(arr[j])   # 해당 길이를 만드는 수열에 마지막 값을 추가해준다. 실수: 리스트에 바로 append를 쓰면 안된다. 변수로 만들고 써야함
                dp_dict[j][1] = dp_dict[k][1] + [arr[j]]


    # 이제 람다함수를 통해서 정렬하고 가장 긴 것을 반환해주기
    # print(dp_dict.items()) # dict_items([(0, [1, [10]]), (1, [2, [10, 20]]), (2, [1, [10]]), (3, [3, [10, 20, 30]]), (4, [2, [10, 20]]), (5, [4, [10, 20, 30, 50]])])
    new_dp_dict = sorted(dp_dict.items(), key=lambda x:x[1][0])  # 리스트속에 튜플이 있는 식으로 정렬된다.
    return new_dp_dict[-1]  # 가장 긴 값을 반환한다.

N = int(input())        # 수열의 크기(1 <= N <= 1,000), 수의 크기 (1 <= Ai <= 1,000)
# 기존 11053_dp_가장긴부분수열과 다른 점은 가장 긴 증가하는 부분 수열길이 뿐아니라, 수열 자체를 출력해야한다는 점이다.
arr = list(map(int, input().split()))
result = dp(N, arr)
print(result[1][0])    # 길이 출력
L = len(result[1][1])
for i in range(L - 1):
    print(result[1][1][i], end=' ')
print(result[1][1][-1])