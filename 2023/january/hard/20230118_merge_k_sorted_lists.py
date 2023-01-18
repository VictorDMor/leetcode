'''
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:
k == lists.length
0 <= k <= 10**4
0 <= lists[i].length <= 500
-10**4 <= lists[i][j] <= 10**4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10**4.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def fill_linked_list(self, flattened_list, list_node):
        if flattened_list == []:
            return list_node
        else:
            list_node.next =  self.fill_linked_list(flattened_list[1:], ListNode(flattened_list[0]))
        return list_node


    def mergeKLists(self, lists):
        final_list = []
        for l in lists:
            while True:
                try:
                    final_list.append(l.val)
                    l = l.next
                except AttributeError:
                    break
        final_list = sorted(final_list)
        if len(final_list) > 0:
            final_linked_list = self.fill_linked_list(final_list[1:], ListNode(final_list[0]))
            return final_linked_list
        return ListNode(None)

list_node_1 = ListNode(1, ListNode(4, ListNode(5)))
list_node_2 = ListNode(1, ListNode(3, ListNode(4)))
list_node_3 = ListNode(2, ListNode(6))
print(Solution().mergeKLists([list_node_1, list_node_2, list_node_3]))
# print(Solution
#         .mergeKLists(Solution(), []))
# print(Solution
#         .mergeKLists(Solution(), [[]]))
