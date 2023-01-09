'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints: 
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Solution without recursion
    def preorderTraversal(self, root):
        output = []
        last_root = []
        while True:
            if root is not None:
                output.append(root.val)
                last_root.append(root)
                root = root.left
            else:
                if len(last_root) > 0:
                    root = last_root[-1].right
                    last_root.pop()
                else:
                    break
        return output

solution = Solution()
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
print(solution.preorderTraversal(node_1))
second_node = TreeNode(None)
print(solution.preorderTraversal(second_node))
third_node = TreeNode(1)
print(solution.preorderTraversal(third_node))