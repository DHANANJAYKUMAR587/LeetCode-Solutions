class Solution(object):
    def countDominantElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        if len(nums)==1:
            return 1
        else:
            for i in range(len(nums)):
                if i==0:
                    if nums[i]>=nums[i+1]:
                        c+=1
                elif i==len(nums)-1:
                    if nums[i]>=nums[i-1]:
                        c+=1
                else:
                    if (nums[i+1]+nums[i-1])<=2*nums[i]:
                        c+=1
            return c