class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=[]
        total = sum(nums)
        for i in nums:
            x=int(''.join(sorted(str(i), reverse=True)))
            ans.append(x-i)
        ans=sorted(ans, reverse=True)
        for i in range(k):
            total+=ans[i]
        return total

