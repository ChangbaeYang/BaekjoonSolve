import sys
input = sys.stdin.readline

def dfs(graph, start_node):
    visited = list()
    need_visit = list()     # 탐색이 필요한 노드 - dfs이므로 stack이 사용될 것이다.
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()     # dfs => stack
        if node not in visited:     # 들린 노드가 아니라면
            visited.append(node)
            gg = sorted(graph[node], reverse=True)    # 내림차순으로 만들기 -> 작은 숫자 먼저
            need_visit.extend(gg)
    return visited

def bfs(graph, start_node):
    visited = list()
    need_visit = list()  # 탐색이 필요한 노드 - bfs이므로 queue이 사용될 것이다.
    need_visit.append(start_node)   # need_visit = [3, 1, 2] 이렇게 들어간다.

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:  # 들린 노드가 아니라면
            visited.append(node)    # 들린 노드로 바꿔준다
            gg = sorted(graph[node])    # 오름차순으로 만들기 -> 작은숫자 먼
            need_visit.extend(gg)
    return visited

N, M, V = map(int, input().split()) # N: 정점개수, M: 간선개수, V: 시작정점
graph = dict()      # graph = { 1 : [2, 3], 2 : [3, 4]} 이런 꼴로 만들 것이다.
for i in range(1, N + 1):
    graph[i] = []

for j in range(M):
    a, b = map(int, input().split())
    # 실수한 점: 정점 사이에 여러 간선이 있는 경우가 있다. -> 중복인 경우 중복을 없애줘야 한다.
    if b not in graph[a]:
        graph[a].append(b)
        graph[b].append(a)
# print(graph)

dfs_visited = dfs(graph, V)
bfs_visited = bfs(graph, V)

for l in range(len(dfs_visited) - 1):
    print(dfs_visited[l], end=' ')
print(dfs_visited[-1])

for k in range(len(bfs_visited) - 1):  # 정점개수로 처리하면 안됌 ㅋㅋ
    print(bfs_visited[k], end=' ')
print(bfs_visited[-1])
