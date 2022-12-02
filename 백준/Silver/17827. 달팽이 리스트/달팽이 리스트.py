import sys

# Node Class를 정리해서 푸는 방법은 시간초과가 났다.
# 그냥 리스트르 풀어봐야겠다.
N, M, V = map(int, sys.stdin.readline().split())
# N: 노드의 개수, M: 질문의 횟수, V: N번의 노드가 가리키는 노드의 번호
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(M):  # 질문의 횟수
    num = int(sys.stdin.readline())    # 첫 노드부터 몇 번 이동했는지 나타내는 변수
    if num < N: # 되돌아오지 않은 경우
        print(arr[num])
    else: # 되돌아오는 경우
        num = (num - N) % (N - V + 1) + V - 1
        print(arr[num])
