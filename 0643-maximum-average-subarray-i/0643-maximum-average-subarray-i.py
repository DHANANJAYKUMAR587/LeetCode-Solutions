class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        Max=float('-inf')
        Sum=0
        for i in range(k):
            Sum+=nums[i]
        Max=Sum
        for  i in range(k,len(nums)):
            Sum=Sum+nums[i]
            Sum=Sum-nums[i-k]
            Max=max(Sum,Max)
        return float(Max)/k