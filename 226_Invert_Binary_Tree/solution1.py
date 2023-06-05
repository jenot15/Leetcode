# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Recrussive Solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            # invert child trees
            self.invertTree(root.left)
            self.invertTree(root.right)

            # swap children 
            temp = root.right
            root.right = root.left
            root.left = temp
        return root

        # n = number of nodes in the tree
        # time complexity = O(n)
        # space complexity = O(n)


        
        