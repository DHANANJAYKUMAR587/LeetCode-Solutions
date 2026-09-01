class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                ans.append(len(set(nums[i:j+1])))
        total=0
        for i in ans:
            total+=i*i
        return total