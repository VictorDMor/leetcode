'''
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 10*9
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if k == 0 or head == None: return head
        def build_list_node(list_node_as_list, list_node):
            if list_node_as_list == []:
                return list_node
            list_node.next = build_list_node(list_node_as_list[1:], ListNode(list_node_as_list[0]))
            return list_node

        list_node_as_list = []
        while True:
            list_node_as_list.append(head.val)
            if head.next is None:
                break
            head = head.next
        for _ in range(k % len(list_node_as_list)):
            list_node_as_list = [list_node_as_list[-1]] + list_node_as_list[:-1]
        
        return build_list_node(list_node_as_list[1:], ListNode(list_node_as_list[0]))