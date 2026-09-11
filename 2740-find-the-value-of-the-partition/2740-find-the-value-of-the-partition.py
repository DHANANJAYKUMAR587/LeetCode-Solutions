class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        ans=float('inf')
        for i in range(len(nums)-1):
            ans=min(ans,abs(nums[i]-nums[i+1]))
        return ans