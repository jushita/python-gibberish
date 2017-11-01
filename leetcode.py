

class Solution():
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])

#Given a binary tree, find its maximum depth.

#The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return (max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1)
