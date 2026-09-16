class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a=max(nums)
        ans=[]
        while k!=0:
            ans.append(a)
            a=a+1
            k-=1
        return sum(ans)