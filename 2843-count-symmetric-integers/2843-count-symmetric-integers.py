class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans=0
        for i in range(low,high+1):
            a=str(i)
            if len(a)%2!=0:
                continue
            mid=len(a)//2
            s=a[:mid]
            e=a[mid:]
            x=0
            n=0
            for j in range(len(s)):
                x+=int(s[j])
            for j in range(len(e)):
                n+=int(e[j])
            if x==n:
                ans+=1
        return ans