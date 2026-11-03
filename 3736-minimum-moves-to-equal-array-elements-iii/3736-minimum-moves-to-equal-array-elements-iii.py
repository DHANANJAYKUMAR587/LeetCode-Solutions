class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=max(nums)
        ans=0
        for i in nums:
            ans+=a-i
        return ans