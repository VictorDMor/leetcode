'''
Daily problem of 2023-01-10

100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10**4 <= Node.val <= 10**4
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        last_node_p = []
        last_node_q = []
        while True:
            if p is not None:
                if q is not None and p.val == q.val:
                    last_node_p.append(p)
                    last_node_q.append(q)
                    p = p.left
                    q = q.left
                else:
                    return False
            elif p is None and q is not None:
                return False
            else:
                if len(last_node_p) > 0:
                    p = last_node_p[-1].right
                    q = last_node_q[-1].right
                    last_node_p.pop()
                    last_node_q.pop()
                else:
                    return True

solution = Solution()
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.left = node_2
node_1.right = node_3
node_4 = TreeNode(1)
node_5 = TreeNode(2)
node_6 = TreeNode(3)
node_4.left = node_5
node_4.right = node_6
print(solution.isSameTree(node_1, node_4))
node_7 = TreeNode(1)
node_8 = TreeNode(2)
node_7.left = node_8
node_9 = TreeNode(1)
node_10 = TreeNode(None)
node_11 = TreeNode(2)
node_9.left = node_10
node_9.right = node_11
print(solution.isSameTree(node_7, node_9))
node_12 = TreeNode(1)
node_13 = TreeNode(2)
node_14 = TreeNode(1)
node_12.left = node_13
node_12.right = node_14
node_15 = TreeNode(1)
node_16 = TreeNode(1)
node_17 = TreeNode(2)
node_15.left = node_16
node_15.right = node_17
print(solution.isSameTree(node_12, node_15))