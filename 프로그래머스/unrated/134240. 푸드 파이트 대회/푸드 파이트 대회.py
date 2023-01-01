def solution(food):
    answer = ''
    sub_answer = ''
    for i in range(1, len(food)):
        a = food[i] // 2    # 음식을 양쪽에 분배할 수 있는 갯수
        answer += str(i) * a
    answer += '0'

    for j in range(len(answer) - 2, -1, -1):
        b = answer[j]
        sub_answer += b
    answer += sub_answer 
    return answer