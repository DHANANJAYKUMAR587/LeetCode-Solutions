class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans=[]
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            if s in ans:
                return True
            ans.append(s)
        return False