class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[]
        for i in range(n+1):
            ans.append(i)
        for i in range(len(ans)):
            if (sum(ans[:len(ans)-i]))==(sum(ans[::-1][:i+1])):
                return(ans[:len(ans)-i][-1])
        return -1