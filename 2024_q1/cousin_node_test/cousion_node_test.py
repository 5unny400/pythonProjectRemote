"""
@FileName：cousion_node_test.py
@Description：
@Author：shenxinyuan
@Time：2024/2/8
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        root.val = 0
        found = 0
        while len(q) > 0:
            q2 = []
            for fa in q:
                if fa.left:
                    q2.append(fa.left)
                if fa.right:
                    q2.append(fa.right)
                if fa.val == x or fa.val == y:
                    if found == 1:
                        return True
                    found = 1
            if found == 1:
                return False
            q = q2
        return False
