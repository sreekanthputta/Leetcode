# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, pathSum):
            if(node.left==None and node.right == None):
                #print(pathSum)
                self.sum += pathSum*10+node.val
            if(node.left!=None):
                helper(node.left, pathSum*10+node.val)
            if(node.right!=None):
                helper(node.right, pathSum*10+node.val)
        
        if(root==None):
            return 0
        helper(root, 0)
        return (self.sum)