"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def build_list_node(ln: Optional[ListNode], support: List) -> ListNode:
            while support != []:
                ln.next = build_list_node(ListNode(val=support.pop(0)), support)
            return ln

        support = []
        while head is not None:
            if head.val not in support:
                support.append(head.val)
            head = head.next
        
        if support != []:
            return build_list_node(ListNode(val=support.pop(0)), support)
        else:
            return None

ln_1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
ln_2 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3)))))
solution = Solution()
print(solution.deleteDuplicates(ln_1))
print(solution.deleteDuplicates(ln_2))