class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total=0
        for i in range(len(nums)):
            a=bin(i)
            if a.count("1")==k:
                total+=nums[i]
        return total