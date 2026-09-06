class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        ans=[]
        for i in nums:
            a=i[0]
            b=i[1]
            for a in range(a,b+1):
                ans.append(a)
        ans=sorted(list(set(ans)))
        a=min(ans)
        b=max(ans)
        result=[]
        for i in range(a,b+1):
            result.append(i)
        return len(result)-(len(result)-len(ans))