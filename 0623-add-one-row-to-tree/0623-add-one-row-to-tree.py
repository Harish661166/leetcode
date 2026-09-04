class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
 
        if depth == 1: return TreeNode(val, root, None)

        level, queue = 2, deque([root])

        while level < depth:
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right)

            level += 1
        
        for node in queue:
            node.left  = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)

        return root