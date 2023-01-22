'''
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        def fill_linked_list(flattened_list, list_node):
            if flattened_list == []:
                return list_node
            else:
                list_node.next =  fill_linked_list(flattened_list[1:], ListNode(flattened_list[0]))
            return list_node

        values_list = []
        while True:
            values_list.append(head.val)
            if head.next == None:
                break
            head = head.next
        final_list = []
        last_i = 0
        if k == len(values_list):
            final_list = values_list[::-1]
        else:
            for i in range(1, len(values_list)+1):
                if i % k == 0:
                    final_list += values_list[i-k:i][::-1]
                    last_i = i
            final_list += values_list[last_i:]
        print(final_list)
        if len(final_list) > 0:
            final_linked_list = fill_linked_list(final_list[1:], ListNode(final_list[0]))
            return final_linked_list
        return ListNode(None)

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    print(Solution().reverseKGroup(head, k))
    k = 3
    print(Solution().reverseKGroup(head, k))
    head = ListNode(8, ListNode(12, ListNode(10, ListNode(9, ListNode(24, ListNode(2))))))
    k = 4
    print(Solution().reverseKGroup(head, k))