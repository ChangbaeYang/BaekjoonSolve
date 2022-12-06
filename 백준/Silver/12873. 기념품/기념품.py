import sys
input = sys.stdin.readline

N = int(input())
arr = [i for i in range(1, N + 1)]
now = [0, 1]     # 현재위치, 외치는 카운팅
t = 1       # 단계설정
while len(arr) > 1:
    L = len(arr)
    R = (t ** 3) % L    # t ** 3 에서 배열의 길이를 나누는 나머지값이 외치는 카운팅 숫자와 같다면 해당 자리를 삭제하면 된다.
    if R == 0:
        R = L
    if now[1] == R:
        del arr[now[0]]
        now[1] = 1      # 지우고나면 1로 초기화
        t += 1      # 다음 단계로 넘어가기
        if now[0] == len(arr):  # 마지막것을 삭제시키며 오른쪽으로 넘어가면 왼쪽으로 보내
            now[0] = 0
    else:   # 지우지 못했다면 한칸 오른쪽으로 가기
        now[0] += 1
        now[1] += 1
        if now[0] == len(arr):  # 오른쪽으로 넘어가버리면 왼쪽으로 보내기
            now[0] = 0
print(arr[0])

