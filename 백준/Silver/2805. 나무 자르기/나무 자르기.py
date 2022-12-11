import sys
input = sys.stdin.readline

# 이진 탐색을 통해 길이를 찾는 것이다.
def binary_search(trees, M):
    max_tree = max(trees)
    start = 1
    end = max_tree
    while end >= start:
        get_tree = 0
        mid = (start + end) // 2
        for tree in trees:      # 자른 후의 나무들을 다 더해준다.
            if tree > mid:
                get_tree += tree - mid
        if get_tree >= M:       # 필요한 나무보다 많이 얻었다면, 절단기 길이를 높여준다.
            start = mid + 1
        else:                   # 필요한 나무보다 적게 얻었다면, 절단기 길이를 낮춰준다.
            end = mid - 1
    return end

N, M = map(int, input().split())            # N : 나무의 수(1 <= N <= 100만), M : 집에 가져가려고 하는 나무의 길이(1 <= M <= 200만)
trees = list(map(int, input().split()))
result = binary_search(trees, M)
print(result)
