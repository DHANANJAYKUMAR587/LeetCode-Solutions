class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=[]
        count=0
        a=s.split("|")
        for i in range(len(a)):
            if i%2==0:
                ans.append(a[i])
        result="".join(ans)
        for i in result:
            if i=="*":
                count+=1
        return count