# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        my_stack = [root]
        while(my_stack):
            current = my_stack.pop()
            self.switch(current)
            
            if current.left:
                my_stack.append(current.left)
            if current.right:
                my_stack.append(current.right)
                

        return root

    def switch(self, node):
        temp = node.left
        node.left=node.right
        node.right=temp