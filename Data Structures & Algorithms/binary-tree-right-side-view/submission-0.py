from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque()

        queue.append(root)

        result = []

        while queue:

            curr_length = len(queue)

            for i in range(curr_length):

                curr_node = queue.popleft()
                if i==curr_length-1:
                    result.append(curr_node.val)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

        return result