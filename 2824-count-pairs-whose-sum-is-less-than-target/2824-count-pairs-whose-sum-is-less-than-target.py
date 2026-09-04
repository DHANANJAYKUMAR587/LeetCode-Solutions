class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        count=0
        i=0
        j=len(nums)-1
        while i<j:
            total=nums[i]+nums[j]
            if total<target:
                count+=(j-i)
                i+=1
            else:
                j-=1
        return count