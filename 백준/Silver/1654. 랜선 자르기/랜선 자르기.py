import sys
input = sys.stdin.readline

K, N = map(int, input().split())    # K: 영식이가 갖고있는 랜선의 갯수, N: 만들어야할 랜선의 갯수
lan = [0] * K   # K개의 랜선의 길이가 담길 리스트
for _ in range(K):
    lan[_] = int(input())
start = 1   # 이분 탐색의 시작점
end = max(lan)  # 이분 탐색의 끝점
while start <= end:
    n = 0   # 잘린 랜선의 총 개수
    mid = (start + end) // 2
    for l in lan:
        n += l // mid
    if n >= N:  # 잘린 개수가 N보다 크거나 같다면(잘게 짤려있다는 뜻) -> 오른쪽 이분 탐색
        start = mid + 1
    else:       # 잘린 개수가 N보다 작다면(너무 크게 잘려있다는 뜻) -> 왼쪽 이분 탐색
        end = mid - 1
print(end)
