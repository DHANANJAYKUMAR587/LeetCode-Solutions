class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums)>1:
            ans=[]
            for i in range(0,len(nums),2):
                if len(ans)%2==0:
                    ans.append(min(nums[i:i+2]))
                else:
                    ans.append(max(nums[i:i+2]))
            nums=ans
        return sum(nums)
