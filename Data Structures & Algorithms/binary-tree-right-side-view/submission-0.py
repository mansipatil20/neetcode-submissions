# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = []
        childs = []
        
        def helperFunction(node, level):
            
            if not node:
                return
            if level == len(childs):
                childs.append([])
            
            childs[level].append(node.val)

            helperFunction(node.left,level+1)
            helperFunction(node.right,level+1)
        helperFunction(root, 0)
        for ele in childs:
            right_view.append(ele[-1])
        return right_view