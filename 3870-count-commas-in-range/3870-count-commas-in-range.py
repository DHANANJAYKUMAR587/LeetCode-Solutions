class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n))<4:
            return 0
        ans=[]
        for i in range(1,n+1):
            if len(str(i))>3:
                ans.append(i)
        return len(ans)