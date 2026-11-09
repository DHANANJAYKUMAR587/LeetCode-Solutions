class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        ans=0
        for i in nums:
            if i==0:
                count+=1
                ans+=count
            else:
                count=0
        return ans