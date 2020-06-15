# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        walker = root
        while(walker!=None and walker.val!=val):
            if(walker.val > val):
                walker = walker.left
            else:
                walker = walker.right
                
        if(walker!=None and walker.val!=val):
            return None
        return walker