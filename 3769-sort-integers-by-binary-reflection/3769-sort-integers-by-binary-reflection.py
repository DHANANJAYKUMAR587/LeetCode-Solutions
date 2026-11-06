class Solution(object):
    def sortByReflection(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in nums:
            a=bin(i)[2:]
            b=a[::-1]
            c=int(b,2)
            ans.append([c,i])
        result=[]
        for i in sorted(ans):
            result.append(i[1])
        return result