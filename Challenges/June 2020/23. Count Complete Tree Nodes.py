# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        if(root.left != None):
            left = self.leftDepth(root.left)
            return self.rec(root, left, left)
        return root.val
            
    def rec(self, root, left, depth):
        if(root.left == None):
            return 1+2**(depth)-1
        right = self.leftDepth(root.right) if(root.right != None) else 0
        if(left > right):
            return self.rec(root.left, left-1, depth)
        else:
            return 2**(right-1)+self.rec(root.right, right-1, depth)
        
    def leftDepth(self, root, len=0):
        if(root == None):
            return 0
        if(root.left != None):
            return self.leftDepth(root.left, len+1)
        return len+1