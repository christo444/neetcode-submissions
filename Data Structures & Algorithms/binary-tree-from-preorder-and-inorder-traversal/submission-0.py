# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_hash_map = {value:index for index,value in enumerate(inorder)}

        self.preorder_index = 0

        def array_to_tree(left_bound,right_bound):

            if left_bound>right_bound:
                return None

            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            inorder_index = inorder_hash_map[root_val]

            self.preorder_index+=1

            root.left = array_to_tree(left_bound,inorder_index-1)

            root.right = array_to_tree(inorder_index+1,right_bound)

            return root

        return array_to_tree(0,len(inorder)-1)