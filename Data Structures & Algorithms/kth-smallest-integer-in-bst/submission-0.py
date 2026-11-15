# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_nodes = []
        def Dfs(node):
            if not node:
                return
            Dfs(node.left)
            tree_nodes.append(node.val)
            Dfs(node.right)
            # tree_nodes.append(node)
        Dfs(root)
        return tree_nodes[k-1]