# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Iterative Approach
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = []
        if root != None:
            que.append(root)

            while(len(que)>0):
                currentNode = que.pop(0)

                # swap children 
                temp = currentNode.right
                currentNode.right = currentNode.left
                currentNode.left = temp

                if (currentNode.left != None):
                    que.append(currentNode.left)
                if (currentNode.right != None):
                    que.append(currentNode.right)

        return root

        # n = number of nodes in the tree
        # time complexity = O(n)
        # space complexity = O(n)


        
        