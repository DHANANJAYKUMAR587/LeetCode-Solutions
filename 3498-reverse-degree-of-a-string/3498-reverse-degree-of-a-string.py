class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0
        a="zyxwvutsrqponmlkjihgfedcba"
        for i in range(len(s)):
            f1=a.index(s[i])+1
            f2=i+1
            total+=(f1*f2)
        return total