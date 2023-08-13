## 2023.08.12 Sat ~ 2023.08.13 Sun 
## 876. 연결 리스트의 중간 부분
### 하나의 연결 리스트의 헤더 부분이 주어졌을 때, 연결 리스트의 가운데 노드(중간노드)를 반환하라.
### 만약 중간 노드가 2개 일때, 두 번째의 중간 노드를 반환한다.

### ========= 코드 시작 부분 =========
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Node = 0
        pre_node = head
        
        while pre_node.next : 
            pre_node = pre_node.next
            Node += 1
        
        half = Node//2 + Node%2
        while half > 0 :
            head = head.next
            half -= 1

        return head
