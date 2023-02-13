'''
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        def build_list_node(list_node, array):
            if array == []:
                return list_node
            list_node.next = build_list_node(ListNode(array[0]), array[1:])
            return list_node

        array = []
        while True:
            array.append(head.val)
            head = head.next
            if head is None:
                break
        array.pop(-n)
        if array == []:
            return None
        return build_list_node(ListNode(array[0]), array[1:])
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))