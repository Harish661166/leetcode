# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def calculate_height(node):
            if not node:
                return 0
            return 1 + max(calculate_height(node.left), calculate_height(node.right))

        height = calculate_height(root)
        m, n = height, 2 ** height - 1
        res = [[""] * n for _ in range(m)]
        res[0][(n-1)//2] = str(root.val)

        def dfs(node, row, col):
            if not node or row + 1 >= height:
                return

            offset = 2 ** (height - row - 2)
            if node.left:
                res[row+1][col-offset] = str(node.left.val)
                dfs(node.left, row+1, col-offset)
            if node.right:
                res[row+1][col+offset] = str(node.right.val)
                dfs(node.right, row+1, col + offset)

        dfs(root, 0, (n-1)//2)
        return res