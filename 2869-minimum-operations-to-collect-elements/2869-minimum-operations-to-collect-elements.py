class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=[]
        for i in range(1,k+1):
            ans.append(i)
        count=0
        for i in range(len(nums)-1,-1,-1):
            count+=1
            if nums[i] in ans:
                ans.remove(nums[i])
            if len(ans)==0:
                return count