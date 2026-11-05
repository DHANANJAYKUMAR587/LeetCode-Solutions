class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)[2:]
        ans=[]
        for idx,val in enumerate(a):
            if val=="1":
                ans.append(idx)
        result=[]
        for i in range(len(ans)-1):
            result.append(ans[i+1]-ans[i])
        if len(result)==0:
            return 0
        else:
            return max(result)