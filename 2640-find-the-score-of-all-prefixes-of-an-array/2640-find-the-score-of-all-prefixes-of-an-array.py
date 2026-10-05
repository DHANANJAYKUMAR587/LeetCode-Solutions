class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        maxi=0
        score=0
        for num in nums:
            maxi=max(maxi,num)
            score+=num+maxi
            ans.append(score)
        return ans