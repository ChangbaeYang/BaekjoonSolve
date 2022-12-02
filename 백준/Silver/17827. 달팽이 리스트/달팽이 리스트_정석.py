import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):    # 마지막 노드에 하나 추가하기
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def last_add(self, data):
        node = self.head
        while node: # 모든 노드에 대해서
            if node.next == None:   # 마지막 노드까지 왔다면 중단시키기
                break
            if node.data == data:   # 노드의 데이터값이 연결될 데이터의 값과 같다면 해당 노드를 마지막 노드의 다음값으로 하기
                target_node = node  # 마지막 노드의 꼬리에 붙일 노드
            node = node.next
        # 반복문을 통해서 나오는 node는 마지막 노드가 된다.
        node.next = target_node

    def desc(self, C):  # 마지막 노드의 데어터 값는 찾는 함수
        node = self.head
        for _ in range(C):
            node = node.next
        return node.data

N, M, V = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
snail = NodeMgmt(arr[0])    # 첫번째 노드를 지정
for i in range(1, N):
    snail.add(arr[i])   # 노드를 한칸씩 미루며 한 노드씩 추가시켜준다.
snail.last_add(arr[V - 1])   # 마지막 노드의 next를 더해주기
# snail.add(arr[V - 1])   -> 이렇게 하면 노드 주소값이 달라진다.

for j in range(M):
    C = int(sys.stdin.readline())
    a = snail.desc(C)
    print(snail.desc(C))