class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans=[]
        A="abcdefghijklmnopqrstuvwxyz"
        D="0123456789"
        for i in strs:
            alp=0
            dig=0
            for j in i:
                if j in A:
                    alp+=1
                elif j in D:
                    dig+=1
            if alp>0:
                ans.append(len(i))
            else:
                ans.append(int(i))
        return max(ans)