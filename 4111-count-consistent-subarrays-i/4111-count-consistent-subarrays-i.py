class Solution(object):
    def countConsistent(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        n=len(nums)
        for i in range(n):
            result=nums[i]
            b=nums[i]
            for j in range(i,n):
                result&=nums[j]
                b=min(b,nums[j])
                if result==b:
                    count+=1
        return count