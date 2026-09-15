class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(1,len(nums)+1):
            a=len(set(nums[:i]))
            b=len(set(nums[i:]))
            ans.append(a-b)
        return ans
