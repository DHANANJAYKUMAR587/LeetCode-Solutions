class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         if (sum(nums[i:j])*len(nums[i:j]))<k:
        #             count+=1
        # return count
        left=0
        total=0
        count=0
        for right in range(len(nums)):
            total+=nums[right]
            while total*(right-left+1)>=k:
                total-=nums[left]
                left+=1
            count+=right-left+1
        return count