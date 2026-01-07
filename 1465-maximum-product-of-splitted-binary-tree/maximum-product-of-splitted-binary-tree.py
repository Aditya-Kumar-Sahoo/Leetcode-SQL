from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Compute total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)
        
        total = total_sum(root)
        
        # Step 2: DFS to compute subtree sums and track max product
        self.best = 0
        
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            # Possible product if we cut above this node
            product = subtree_sum * (total - subtree_sum)
            if product > self.best:
                self.best = product
            return subtree_sum
        
        dfs(root)
        return self.best % MOD