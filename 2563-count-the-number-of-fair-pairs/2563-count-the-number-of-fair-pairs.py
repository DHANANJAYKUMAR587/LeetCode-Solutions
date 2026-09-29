class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]>=lower and nums[i]+nums[j]<=upper:
        #             count+=1
        # return count
        def pairs(nums,target):
            nums.sort()
            count=0
            i=0
            j=len(nums)-1
            while i<=j:
                if nums[i]+nums[j]<=target:
                    count+=j-i
                    i+=1
                else:
                    j-=1
            return count
        ans=pairs(nums,upper)-pairs(nums,lower-1)
        return ans