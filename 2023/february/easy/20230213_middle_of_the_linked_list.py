'''
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def middleNode(self, head):
        def build_list_node(list_node, array):
            if array == []:
                return list_node
            list_node.next = build_list_node(ListNode(array[0]), array[1:])
            return list_node

        node_list = []
        while True:
            node_list.append(head.val)
            if head.next is None:
                break
            head = head.next
        
        if len(node_list) % 2 == 0:
            middle = node_list[int(len(node_list)/2):]
        else:
            middle = node_list[math.floor(len(node_list)/2):]
        
        return build_list_node(ListNode(middle[0]), middle[1:])