class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        Min=10**9
        Sum=0
        j=0
        i=0
        while j<len(nums):
            Sum=Sum+nums[j]
            while Sum>=target:
                Min=min(Min,j-i+1)
                Sum=Sum-nums[i]
                i+=1
            j+=1
        if Min == 10**9:
            return 0 
        else:
            return Min