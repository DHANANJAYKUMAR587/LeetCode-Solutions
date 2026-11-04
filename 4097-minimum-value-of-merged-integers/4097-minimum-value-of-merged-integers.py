class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Min=float("inf")
        for i in range(0,len(nums)-1,2):
            a=str(nums[i])
            b=str(nums[i+1])
            if int(a+b)<Min:
                Min=int(a+b)
        return Min