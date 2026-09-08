class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                a=max(str(nums[i]))
                b=max(str(nums[j]))
                if a==b:
                    ans.append(nums[i]+nums[j])
        if len(ans)==0:
            return -1
        else:
            return max(ans)