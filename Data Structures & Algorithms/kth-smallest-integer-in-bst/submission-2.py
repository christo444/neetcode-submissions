# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # stack = []
        # curr = root

        # while stack or curr:

        #     while curr:
        #         stack.append(curr)
        #         curr=curr.left

        #     curr = stack.pop()
        #     k-=1

        #     if k==0:
        #         return curr.val

        #     curr = curr.right


        self.k = k
        self.res = None

        def inorder(node):

            if not node or self.res is not None:
                return

            inorder(node.left)

            self.k-=1
            if self.k==0:
                self.res = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.res

