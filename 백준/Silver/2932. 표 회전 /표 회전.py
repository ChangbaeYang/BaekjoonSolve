import sys
input = sys.stdin.readline

# N : N * N 표, N: 표의크기/ K : 이동시키려는 숫자의 수
N, K = map(int, input().split())

target_list = []   # (num, 목표지점의 행, 목표지점의 열) 튜플 사용이유 : 목표지점은 변하지 않기 때문에
# now_list = [0] * 100000001   # [num, 현재위치의 행, 현재위치의 열], 카운팅정렬
# -> 메모리 초과 난다. 배열의 크기가 너 커버린다.
now_list = {}   # 딕셔너리를 활용해서, 해쉬 테이블의 장점을 활용하고자 했습니다 -> 빠른 탐색이 가능
num_list = []   # 체크할 번호들을 담는 리스트
now_check_list = []     # 한점을 여러번 리딩하는 것을 방지하는 리스트 -> 예제 입력 중에 6을 2번 움직여야하는 경우를 발견했음.
# 준비단계
for _ in range(K):
    num, x, y = map(int, input().split())
    num_list.append(num)
    target_list.append((num, x, y)) # 목표지점은 바뀌지 않기 때문에 튜플로 추가 했습니다.
    # 아래는 찾은 규칙성을 바탕으로 쓴 코드
    d = num // N    # 몫 -> 행을 구하기 위함
    r = num % N     # 나머지 -> 열을 구하기 위함
    if r == 0:      # 맨 오른쪽 열에 있는 번호들의 경우 몫은 그대로 유지, 나머지는 N만큼 추가
        b = N       # [num, a, b]를 통해 now_list를 채울 것이다.
        a = d       # a는 열, b는 행을 의미한다.
    else:       # 위의 경우가 아닌 경우에는 몫은 하나 더해주고, 나머지는 그대로 유지시킨다.
        b = r
        a = d + 1
    if num not in now_check_list:
        now_check_list.append(num)  # 6이 2번 now_list에 들어가는 것을 방지
        now_list[num] = [a, b]  # {num : [a, b]} 로 집어넣는다.

for target in target_list: # 목표지점하나씩 순회하면서 현재위치와 비교
    count = 0
    dx = target[1] - now_list[target[0]][0]    # target[0]은 이동시키고 있는 번호
    dy = target[2] - now_list[target[0]][1]
    if dx < 0:  # 아래로만 이동하기 때문에 -> 양수화
        dx += N
    if dy < 0:  # 오른쪽으로만 이동하기 때문에 -> 양수화
        dy += N
    # 행이 같으면 열이동 - 체크 중인 점 포함
    for check in now_check_list:
        if now_list[target[0]][0] == now_list[check][0]:    # 현재 체크중인 번호와 행이 같다면 위치 이동
            now_list[check][1] += dy        # dy만큼 이동시키기(오른쪽으로)
            if now_list[check][1] > N:     # 칸 넘어가면 왼쪽으로 보내기
                now_list[check][1] -= N
    count += dy # 이동한 열만큼 더해준다.
    # 열이 같으면 행이동
    for check in now_check_list:
        if now_list[target[0]][1] == now_list[check][1]:    # 현재 체크중인 번호와 열이 같다면 위치이동
            now_list[check][0] += dx        # dx만큼 이동시키기(아래로)
            if now_list[check][0] > N:      # 칸 넘어가면 위로 보내기
                now_list[check][0] -= N
    count += dx # 이동한 행만큼 더해준다.

    print(count)