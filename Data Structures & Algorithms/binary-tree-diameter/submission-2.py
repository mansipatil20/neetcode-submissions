# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node) -> int:
            nonlocal diameter
            if node == None:
                return -1
            left_height = 1 + dfs(node.left)
            right_height = 1 + dfs(node.right)

            # candidate = left_height + right_height
            candidate = left_height + right_height
            diameter = max(diameter,candidate)
            return max(left_height, right_height)
        dfs(root)
        return diameter